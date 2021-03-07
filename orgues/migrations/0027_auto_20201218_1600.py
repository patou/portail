# Generated by Django 2.2.13 on 2020-12-18 16:00

from django.db import migrations, models
import orgues.models


class Migration(migrations.Migration):

    dependencies = [
        ('orgues', '0026_auto_20201130_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(help_text='Taille maximale : 2 Mo. Les images doivent être libres de droits.', upload_to=orgues.models.chemin_image),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='tirage_jeux',
            field=models.CharField(blank=True, choices=[('mecanique', 'Mécanique'), ('pneumatique_haute_pression', 'Pneumatique haute pression'), ('pneumatique_basse_pression', 'Pneumatique basse pression'), ('electrique', 'Electrique'), ('electro_pneumatique', 'Electro-pneumatique')], max_length=30, null=True, verbose_name='Tirage des jeux'),
        ),
    ]
