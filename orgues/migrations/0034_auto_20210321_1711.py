# Generated by Django 2.2.7 on 2021-03-21 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgues', '0033_auto_20210320_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='order',
            field=models.IntegerField(default=0, verbose_name="Ordre d'affichage"),
        ),
        migrations.AlterField(
            model_name='evenement',
            name='annee_fin',
            field=models.IntegerField(blank=True, help_text='Optionnelle', null=True, verbose_name="Année de fin de l'évènement"),
        ),
        migrations.AlterField(
            model_name='evenement',
            name='circa',
            field=models.BooleanField(default=False, verbose_name='Cocher si dates approximatives'),
        ),
    ]
