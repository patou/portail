# Generated by Django 2.2.6 on 2019-11-08 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import orgues.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clavier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_expressif', models.BooleanField(default=False, verbose_name='Cocher si expressif')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Update date')),
            ],
        ),
        migrations.CreateModel(
            name='Facteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TypeClavier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Type de clavier',
                'verbose_name_plural': 'Types de claviers',
            },
        ),
        migrations.CreateModel(
            name='TypeJeu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('hauteur', models.CharField(help_text='La hauteur est indiquée par convention en pieds, en chiffres arabes, sans précision de l\'unité. La nombre de rangs des fournitures, plein-jeux, cornet, etc. est indiqué en chiffre romains, sans précision du terme "rangs" (ni "rgs").', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Types de jeux',
            },
        ),
        migrations.CreateModel(
            name='Orgue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(default='Orgue', max_length=300, verbose_name='Désignation')),
                ('codification', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, help_text='Description générale')),
                ('proprietaire', models.CharField(choices=[('commune', 'Commune'), ('Etat', 'Etat'), ('association culturelle', 'Association culturelle'), ('diocèse', 'Diocèse'), ('paroisse', 'Paroisse')], default='commune', max_length=20)),
                ('association', models.CharField(blank=True, help_text="Nom de l'association en charge de l'instrument", max_length=100, null=True)),
                ('association_lien', models.URLField(blank=True, help_text="Lien vers le site de l'association", max_length=300, null=True)),
                ('is_polyphone', models.BooleanField(default=False, verbose_name='Orgue polyphone de la manufacture Debierre ?')),
                ('etat', models.CharField(blank=True, choices=[('bon', 'Très bon ou bon : tout à fait jouable'), ('altere', 'Altéré : difficilement jouable'), ('degrade', 'Dégradé ou en ruine : injouable')], max_length=20, null=True)),
                ('elevation', models.CharField(blank=True, choices=[('sol', 'Au sol'), ('tribune', 'En tribune')], max_length=20, null=True)),
                ('buffet', models.TextField(blank=True, help_text='Description du buffet et de son état', null=True)),
                ('console', models.TextField(blank=True, help_text="Description de la console (ex: en fenêtre, séparée organiste tourné vers l'orgue ...)", null=True)),
                ('commentaire_admin', models.TextField(blank=True, help_text="Ce commentaire n'est visible qu'en mode édition", null=True)),
                ('edifice', models.CharField(max_length=300)),
                ('commune', models.CharField(max_length=100)),
                ('code_insee', models.CharField(max_length=200)),
                ('ancienne_commune', models.CharField(blank=True, max_length=100, null=True)),
                ('departement', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('diapason', models.CharField(blank=True, help_text='Hauteur en Hertz du A2 joué par le prestant 4', max_length=15, null=True)),
                ('sommiers', models.TextField(blank=True, null=True)),
                ('soufflerie', models.TextField(blank=True, null=True)),
                ('transmission_notes', models.CharField(blank=True, choices=[('mecanique', 'Mécanique'), ('mecanique_suspendue', 'Mécanique suspendue'), ('mecanique_barker', 'Mécanique Barker'), ('pneumatique', 'Pneumatique'), ('electrique', 'Electrique')], max_length=20, null=True)),
                ('tirage_jeux', models.CharField(blank=True, choices=[('mecanique', 'Mécanique'), ('pneumatique', 'Pneumatique'), ('electrique', 'Electrique')], max_length=20, null=True)),
                ('commentaire_tuyauterie', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('slug', models.SlugField(max_length=255)),
                ('completion', models.IntegerField(default=False, editable=False)),
                ('updated_by_user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Jeu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentaire', models.CharField(blank=True, max_length=200, null=True)),
                ('clavier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jeux', to='orgues.Clavier')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jeux', to='orgues.TypeJeu')),
            ],
            options={
                'verbose_name_plural': 'Jeux',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=orgues.models.chemin_image)),
                ('is_principale', models.BooleanField(default=False, editable=False)),
                ('credit', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('orgue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='orgues.Orgue')),
            ],
        ),
        migrations.CreateModel(
            name='Fichier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=orgues.models.chemin_fichier, verbose_name='Fichier')),
                ('description', models.CharField(max_length=100, verbose_name='Nom de fichier à afficher')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('orgue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fichiers', to='orgues.Orgue')),
            ],
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee', models.IntegerField(verbose_name='Année')),
                ('type', models.CharField(choices=[('construction', 'Construction'), ('reconstruction', 'Reconstruction'), ('destruction', 'Destruction'), ('restauration', 'Restauration'), ('demenagement', 'Déménagement'), ('relevage', 'Relevage'), ('disparition', 'Disparition'), ('degats', 'Dégâts'), ('classement_mh', 'Classement aux monuments historiques'), ('inscription_mh', 'Inscription aux monuments historiques')], max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('facteurs', models.ManyToManyField(blank=True, to='orgues.Facteur')),
                ('orgue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evenements', to='orgues.Orgue')),
            ],
            options={
                'ordering': ['annee'],
            },
        ),
        migrations.AddField(
            model_name='clavier',
            name='facteur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orgues.Facteur'),
        ),
        migrations.AddField(
            model_name='clavier',
            name='orgue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='claviers', to='orgues.Orgue'),
        ),
        migrations.AddField(
            model_name='clavier',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orgues.TypeClavier'),
        ),
    ]
