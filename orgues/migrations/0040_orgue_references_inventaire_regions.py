# Generated by Django 2.2.13 on 2021-05-04 12:00
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgues', '0039_auto_20210423_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgue',
            name='references_inventaire_regions',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Code inventaire régional'),
        ),
    ]
