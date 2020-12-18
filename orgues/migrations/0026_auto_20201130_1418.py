# Generated by Django 2.2.13 on 2020-11-30 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgues', '0025_auto_20201117_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgue',
            name='tirage_jeux',
            field=models.CharField(blank=True, choices=[('mecanique', 'Mécanique'), ('pneumatique_haute_pression', 'Pneumatique haute pression'), ('pneumatique_basse_pression', 'Pneumatique basse pression'), ('electrique', 'Electrique'), ('electro_pneumatique', 'Electro-pneumatique')], max_length=20, null=True, verbose_name='Tirage des jeux'),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='transmission_notes',
            field=models.CharField(blank=True, choices=[('mecanique', 'Mécanique'), ('mecanique_suspendue', 'Mécanique suspendue'), ('mecanique_balanciers', 'Mécanique à balanciers'), ('mecanique_barker', 'Mécanique Barker'), ('electrique', 'Electrique'), ('electrique_proportionnelle', 'Electrique proportionnelle'), ('electro_pneumatique', 'Electro-pneumatique'), ('pneumatique', 'Pneumatique')], max_length=30, null=True, verbose_name='Transmission des notes'),
        ),
    ]