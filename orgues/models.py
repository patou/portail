import json
import os
import uuid
from django.db import models
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

from accounts.models import User


class Facteur(models.Model):
    """
    Pas celui qui distribue le courrier
    """
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Orgue(models.Model):
    CHOIX_PROPRIETAIRE = (
        ("commune", "Commune"),
        ("Etat", "Etat"),
        ("association culturelle", "Association culturelle"),
        ("diocèse", "Diocèse"),
        ("paroisse", "Paroisse"),
    )

    CHOIX_ETAT = (
        ('bon', "Très bon ou bon : tout à fait jouable"),
        ('altere', "Altéré : difficilement jouable"),
        ('degrade', "Dégradé ou en ruine : injouable"),
    )

    CHOIX_ELEVATION = (
        ('sol', "Au sol"),
        ('tribune', "En tribune"),
    )

    CHOIX_TRANSMISSION = (
        ("mecanique", "Mécanique"),
        ("mecanique_suspendue", "Mécanique suspendue"),
        ("mecanique_barker", "Mécanique Barker"),
        ("pneumatique", "Pneumatique"),
        ("electrique", "Electrique"),
    )

    CHOIX_TIRAGE = (
        ("mecanique", "Mécanique"),
        ("pneumatique", "Pneumatique"),
        ("electrique", "Electrique"),
    )
    CHOIX_DESIGNATION = (
        ("grand_orgue", "Grand orgue"),
        ("orgue_choeur", "Orgue de chœur"),
        ("orgue", "Orgue")
    )
    # Informations générales

    designation = models.CharField(max_length=300, verbose_name="Désignation",choices=CHOIX_DESIGNATION, default="Orgue")
    codification = models.CharField(max_length=100)
    description = models.TextField(blank=True, help_text="Description générale")
    proprietaire = models.CharField(max_length=20, choices=CHOIX_PROPRIETAIRE, default="commune")
    association = models.CharField(max_length=100, null=True, blank=True,
                                   help_text="Nom de l'association en charge de l'instrument")
    association_lien = models.URLField(max_length=300, null=True, blank=True,
                                       help_text="Lien vers le site de l'association")
    is_polyphone = models.BooleanField(default=False, verbose_name="Orgue polyphone de la manufacture Debierre ?")
    etat = models.CharField(max_length=20, choices=CHOIX_ETAT, null=True, blank=True)
    elevation = models.CharField(max_length=20, choices=CHOIX_ELEVATION, null=True, blank=True,verbose_name="Elévation")
    buffet = models.TextField(null=True, blank=True, help_text="Description du buffet et de son état")
    console = models.TextField(null=True, blank=True,
                               help_text="Description de la console (ex: en fenêtre, séparée organiste tourné vers l'orgue ...)")

    commentaire_admin = models.TextField(null=True, blank=True,
                                         help_text="Ce commentaire n'est visible qu'en mode édition")

    # Géographie
    edifice = models.CharField(max_length=300)
    commune = models.CharField(max_length=100)
    code_insee = models.CharField(max_length=200)
    ancienne_commune = models.CharField(max_length=100, null=True, blank=True)
    departement = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    # Tuyauterie
    diapason = models.CharField(max_length=15, null=True, blank=True,
                                help_text="Hauteur en Hertz du A2 joué par le prestant 4")
    sommiers = models.TextField(null=True, blank=True)
    soufflerie = models.TextField(null=True, blank=True)
    transmission_notes = models.CharField(max_length=20, choices=CHOIX_TRANSMISSION, null=True, blank=True)
    tirage_jeux = models.CharField(max_length=20, choices=CHOIX_TIRAGE, null=True, blank=True)
    commentaire_tuyauterie = models.TextField(blank=True)

    # Auto générés

    created_date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Creation date')
    modified_date = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Update date')
    updated_by_user = models.ForeignKey(User, null=True, editable=False, on_delete=models.SET_NULL)
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, unique=True, editable=False)
    slug = models.SlugField(max_length=255)
    completion = models.IntegerField(default=False, editable=False)

    def __str__(self):
        return self.designation

    class Meta:
        ordering = ['-created_date']

    def save(self, *args, **kwargs):
        self.completion = self.calcul_completion()
        super().save(*args, **kwargs)

    @property
    def image_principale(self):
        """
        Récupère l'image principale de l'instrument
        """
        return self.images.filter(is_principale=True).first()

    @property
    def has_pedalier(self):
        """
        Est-ce que l'instrument possède un pédalier ?
        """
        return self.claviers.filter(type__nom="Pédalier").exists()

    @property
    def facteurs(self):
        """
        Liste des facteurs ayant participé à la construction de l'instrument
        """
        construction = self.evenements.filter(type="construction").first()
        if construction:
            return construction.facteurs.all()

    @property
    def jeux_count(self):
        """
        Nombre de jeux de l'instrument
        """
        return Jeu.objects.filter(clavier__orgue=self).count()

    def get_absolute_url(self):
        return reverse('orgues:orgue-detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('orgues:orgue-update', args=(self.uuid,))

    def get_delete_url(self):
        return reverse('orgues:orgue-delete', args=(self.uuid,))

    def calcul_completion(self):
        """
        Pourcentage de remplissage de la fiche instrument
        """
        points = 0
        champs_importants = [
            self.designation,
            self.description,
            self.proprietaire,
            self.association,
            self.association_lien,
            self.etat,
            self.elevation,
            self.buffet,
            self.console,
            self.edifice,
            self.commune,
            self.departement,
            self.region,
            self.latitude,
            self.longitude,
            self.diapason,
            self.sommiers,
            self.soufflerie,
            self.transmission_notes,
            self.tirage_jeux,
        ]

        for champ in champs_importants:
            if champ:
                points += 1

        if self.claviers.count():
            points += 5

        if self.evenements.filter(type="construction", facteurs__isnull=False):
            points += 3

        if self.images.filter(is_principale=True):
            points += 5

        points_max = len(champs_importants) + 5 + 3 + 5

        return int(100 * points / points_max)


class TypeClavier(models.Model):
    """
    Type de clavier
    Ex :
    Grand Orgue
    Récit
    Pédalier
    """
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Type de clavier"
        verbose_name_plural = "Types de claviers"


class Clavier(models.Model):
    """
    Un orgue peut avoir plusieurs clavier
    """

    type = models.ForeignKey(TypeClavier, null=True, on_delete=models.CASCADE)
    facteur = models.ForeignKey(Facteur, null=True, blank=True, on_delete=models.SET_NULL)
    is_expressif = models.BooleanField(verbose_name="Cocher si expressif", default=False)

    # Champs automatiques
    orgue = models.ForeignKey(Orgue, null=True, on_delete=models.CASCADE, related_name="claviers")
    created_date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        verbose_name='Creation date'
    )
    modified_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        verbose_name='Update date'
    )

    def __str__(self):
        return "{} | {}".format(self.type.nom, self.orgue.designation)


class Evenement(models.Model):
    """
    Décrit les différents événements relatifs à un orgue

    Les événements sont affichés via le plugin : https://timeline.knightlab.com/

    Relavage : simple opération de conservation de l'instrument, menée à intervalles réguliers.
    Reconstruction : des éléments nouveaux sont ajoutés en grand nombre, la structure de l'instrument est modifiée.
    Restauration : opération d'importance, à caractère patrimonial : il s'agit de revenir à un état antérieur de l'instrument.
    Destruction : dégâts sur l'ensemble de l'instrument, rendu totalement inutilisable.
    Disparition : distincte de destruction, car l'orgue a pu disparaître suit à un déménagement, ou être stocké dans un endroit inconnu.

    """

    CHOIX_TYPE = (
        ("construction", "Construction"),
        ("reconstruction", "Reconstruction"),
        ("destruction", "Destruction"),
        ("restauration", "Restauration"),
        ("demenagement", "Déménagement"),
        ("relevage", "Relevage"),
        ("disparition", "Disparition"),
        ("degats", "Dégâts"),
        ("classement_mh", "Classement aux monuments historiques"),
        ("inscription_mh", "Inscription aux monuments historiques"),
    )

    annee = models.IntegerField(verbose_name="Année")
    type = models.CharField(max_length=20, choices=CHOIX_TYPE)
    facteurs = models.ManyToManyField(Facteur, blank=True)
    description = models.TextField(blank=True, null=True)

    # Champs automatiques
    orgue = models.ForeignKey(Orgue, on_delete=models.CASCADE, related_name="evenements")

    def __str__(self):
        return "{} ({})".format(self.type, self.annee)

    class Meta:
        ordering = ["annee"]


    @property
    def facteurs_str(self):
        return ",".join(self.facteurs.values_list("nom",flat=True))


class TypeJeu(models.Model):
    """
    Lorsque l'on définit les jeux d'un clavier, on pioche parmi les types de jeu existants
    """
    nom = models.CharField(max_length=50)
    hauteur = models.CharField(max_length=20,
                               help_text="La hauteur est indiquée par convention en pieds, en chiffres arabes, "
                                         "sans précision de l'unité. La nombre de rangs des fournitures, plein-jeux,"
                                         " cornet, etc. est indiqué en chiffre romains,"
                                         " sans précision du terme \"rangs\" (ni \"rgs\").")

    def __str__(self):
        return "{} {}".format(self.nom, self.hauteur)

    class Meta:
        verbose_name_plural = "Types de jeux"


class Jeu(models.Model):
    type = models.ForeignKey(TypeJeu, on_delete=models.CASCADE, related_name='jeux')
    commentaire = models.CharField(max_length=200, null=True, blank=True)
    clavier = models.ForeignKey(Clavier, null=True, on_delete=models.CASCADE, related_name="jeux")

    def __str__(self):
        return str(self.type)

    class Meta:
        verbose_name_plural = "Jeux"


def chemin_fichier(instance, filename):
    return os.path.join(slugify(instance.orgue.edifice), "fichiers", filename)


class Fichier(models.Model):
    """
    Fichiers liées à un instrument
    """
    file = models.FileField(upload_to=chemin_fichier, verbose_name="Fichier")
    description = models.CharField(max_length=100, verbose_name="Nom de fichier à afficher")
    orgue = models.ForeignKey(Orgue, null=True, on_delete=models.CASCADE, related_name="fichiers")

    # Champs automatiques
    created_date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        verbose_name='Creation date'
    )
    modified_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        verbose_name='Update date'
    )


def chemin_image(instance, filename):
    return os.path.join(slugify(instance.orgue.edifice), "fichiers", filename)


class Image(models.Model):
    """
    Images liées à un instrument
    """
    image = models.ImageField(upload_to=chemin_image)
    is_principale = models.BooleanField(default=False, editable=False)
    credit = models.CharField(max_length=200, null=True, blank=True)

    # Champs automatiques
    thumbnail = ImageSpecField(source='image',
                               processors=[ResizeToFill(400, 300)],
                               format='JPEG',
                               options={'quality': 80})
    vignette = ImageSpecField(source='image',
                              processors=[ResizeToFill(150, 100)],
                              format='JPEG',
                              options={'quality': 80})

    orgue = models.ForeignKey(Orgue, null=True, on_delete=models.CASCADE, related_name="images")
    created_date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        verbose_name='Creation date'
    )
    modified_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        verbose_name='Update date'
    )