# Generated by Django 2.2.13 on 2021-04-14 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgues', '0037_merge_20210413_1820'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facteur',
            options={'ordering': ['latitude_atelier']},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['order', 'created_date']},
        ),
        migrations.AddField(
            model_name='clavier',
            name='commentaire',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='departement',
            field=models.CharField(choices=[('Ain', 'Ain'), ('Aisne', 'Aisne'), ('Allier', 'Allier'), ('Alpes-de-Haute-Provence', 'Alpes-de-Haute-Provence'), ('Hautes-Alpes', 'Hautes-Alpes'), ('Alpes-Maritimes', 'Alpes-Maritimes'), ('Ardèche', 'Ardèche'), ('Ardennes', 'Ardennes'), ('Ariège', 'Ariège'), ('Aube', 'Aube'), ('Aude', 'Aude'), ('Aveyron', 'Aveyron'), ('Bouches-du-Rhône', 'Bouches-du-Rhône'), ('Calvados', 'Calvados'), ('Cantal', 'Cantal'), ('Charente', 'Charente'), ('Charente-Maritime', 'Charente-Maritime'), ('Cher', 'Cher'), ('Corrèze', 'Corrèze'), ('Corse-du-Sud', 'Corse-du-Sud'), ('Haute-Corse', 'Haute-Corse'), ("Côte-d'Or", "Côte-d'Or"), ("Côtes-d'Armor", "Côtes-d'Armor"), ('Creuse', 'Creuse'), ('Dordogne', 'Dordogne'), ('Doubs', 'Doubs'), ('Drôme', 'Drôme'), ('Eure', 'Eure'), ('Eure-et-Loir', 'Eure-et-Loir'), ('Finistère', 'Finistère'), ('Gard', 'Gard'), ('Haute-Garonne', 'Haute-Garonne'), ('Gers', 'Gers'), ('Gironde', 'Gironde'), ('Hérault', 'Hérault'), ('Ille-et-Vilaine', 'Ille-et-Vilaine'), ('Indre', 'Indre'), ('Indre-et-Loire', 'Indre-et-Loire'), ('Isère', 'Isère'), ('Jura', 'Jura'), ('Landes', 'Landes'), ('Loir-et-Cher', 'Loir-et-Cher'), ('Loire', 'Loire'), ('Haute-Loire', 'Haute-Loire'), ('Loire-Atlantique', 'Loire-Atlantique'), ('Loiret', 'Loiret'), ('Lot', 'Lot'), ('Lot-et-Garonne', 'Lot-et-Garonne'), ('Lozère', 'Lozère'), ('Maine-et-Loire', 'Maine-et-Loire'), ('Manche', 'Manche'), ('Marne', 'Marne'), ('Haute-Marne', 'Haute-Marne'), ('Mayenne', 'Mayenne'), ('Meurthe-et-Moselle', 'Meurthe-et-Moselle'), ('Meuse', 'Meuse'), ('Morbihan', 'Morbihan'), ('Moselle', 'Moselle'), ('Nièvre', 'Nièvre'), ('Nord', 'Nord'), ('Oise', 'Oise'), ('Orne', 'Orne'), ('Pas-de-Calais', 'Pas-de-Calais'), ('Puy-de-Dôme', 'Puy-de-Dôme'), ('Pyrénées-Atlantiques', 'Pyrénées-Atlantiques'), ('Hautes-Pyrénées', 'Hautes-Pyrénées'), ('Pyrénées-Orientales', 'Pyrénées-Orientales'), ('Bas-Rhin', 'Bas-Rhin'), ('Haut-Rhin', 'Haut-Rhin'), ('Rhône', 'Rhône'), ('Haute-Saône', 'Haute-Saône'), ('Saône-et-Loire', 'Saône-et-Loire'), ('Sarthe', 'Sarthe'), ('Savoie', 'Savoie'), ('Haute-Savoie', 'Haute-Savoie'), ('Paris', 'Paris'), ('Seine-Maritime', 'Seine-Maritime'), ('Seine-et-Marne', 'Seine-et-Marne'), ('Yvelines', 'Yvelines'), ('Deux-Sèvres', 'Deux-Sèvres'), ('Somme', 'Somme'), ('Tarn', 'Tarn'), ('Tarn-et-Garonne', 'Tarn-et-Garonne'), ('Var', 'Var'), ('Vaucluse', 'Vaucluse'), ('Vendée', 'Vendée'), ('Vienne', 'Vienne'), ('Haute-Vienne', 'Haute-Vienne'), ('Vosges', 'Vosges'), ('Yonne', 'Yonne'), ('Territoire de Belfort', 'Territoire de Belfort'), ('Essonne', 'Essonne'), ('Hauts-de-Seine', 'Hauts-de-Seine'), ('Seine-Saint-Denis', 'Seine-Saint-Denis'), ('Val-de-Marne', 'Val-de-Marne'), ("Val-d'Oise", "Val-d'Oise"), ('Guadeloupe', 'Guadeloupe'), ('Martinique', 'Martinique'), ('Mayotte', 'Mayotte'), ('Guyane', 'Guyane'), ('La Réunion', 'La Réunion'), ('Saint-Pierre-et-Miquelon', 'Saint-Pierre-et-Miquelon'), ('Nouvelle-Calédonie', 'Nouvelle-Calédonie')], max_length=50, verbose_name='Département'),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='etat',
            field=models.CharField(blank=True, choices=[('tres_bon', 'Très bon, tout à fait jouable'), ('bon', 'Bon : jouable, défauts mineurs'), ('altere', 'Altéré : difficilement jouable'), ('degrade', 'Dégradé ou en ruine : injouable'), ('restauration', 'En restauration (ou projet initié)')], help_text="Se rapporte au fait que l'orgue est jouable ou non.", max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='proprietaire',
            field=models.CharField(choices=[('commune', 'Commune'), ('interco', 'Intercommunalité'), ('etat', 'Etat'), ('association_culturelle', 'Association culturelle'), ('diocese', 'Diocèse'), ('paroisse', 'Paroisse'), ('congregation', 'Congrégation'), ('etablissement_scolaire', 'Etablissement scolaire'), ('conservatoire', 'Conservatoire ou Ecole de musique'), ('hopital', 'Hôpital')], default='commune', max_length=40, null=True, verbose_name='Propriétaire'),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='tirage_jeux',
            field=models.CharField(blank=True, choices=[('mecanique', 'Mécanique'), ('pneumatique_haute_pression', 'Pneumatique haute pression'), ('pneumatique_basse_pression', 'Pneumatique basse pression'), ('numerique', 'Numérique'), ('electrique', 'Electrique'), ('electro_pneumatique', 'Electro-pneumatique')], max_length=30, null=True, verbose_name='Tirage des jeux'),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='transmission_notes',
            field=models.CharField(blank=True, choices=[('mecanique', 'Mécanique'), ('mecanique_suspendue', 'Mécanique suspendue'), ('mecanique_balanciers', 'Mécanique à balanciers'), ('mecanique_barker', 'Mécanique Barker'), ('numerique', 'Numérique'), ('electrique', 'Electrique'), ('electrique_proportionnelle', 'Electrique proportionnelle'), ('electro_pneumatique', 'Electro-pneumatique'), ('pneumatique', 'Pneumatique')], max_length=30, null=True, verbose_name='Transmission des notes'),
        ),
        migrations.AlterField(
            model_name='typejeu',
            name='hauteur',
            field=models.CharField(blank=True, help_text='La hauteur est indiquée par convention en pieds, en chiffres arabes, sans précision de l\'unité. La nombre de rangs des fournitures, plein-jeux, cornet, etc. est indiqué en chiffres romains, sans précision du terme "rangs" (ni "rgs").', max_length=20, null=True),
        ),
    ]