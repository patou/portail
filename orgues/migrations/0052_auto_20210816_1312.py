# Generated by Django 3.1.12 on 2021-08-16 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgues', '0051_auto_20210813_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='type',
            field=models.CharField(choices=[('construction', 'Construction'), ('inauguration', 'Inauguration'), ('reconstruction', 'Reconstruction'), ('destruction', 'Destruction'), ('restauration', 'Restauration'), ('deplacement', 'Déplacement'), ('demontage', 'Démontage et stockage'), ('relevage', 'Relevage'), ('modifications', 'Modifications'), ('disparition', 'Disparition'), ('degats', 'Dégâts'), ('classement_mh', 'Classement au titre des monuments historiques'), ('inscription_mh', 'Inscription au titre des monuments historiques')], max_length=20),
        ),
        migrations.AlterField(
            model_name='jeu',
            name='configuration',
            field=models.CharField(blank=True, choices=[('basse', 'Basse'), ('dessus', 'Dessus'), ('basse_et_dessus', 'Basse et Dessus')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='designation',
            field=models.CharField(blank=True, default='orgue', max_length=300, null=True, verbose_name="Désignation de l'orgue"),
        ),
    ]
