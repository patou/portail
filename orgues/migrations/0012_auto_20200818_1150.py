# Generated by Django 2.2.7 on 2020-08-18 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgues', '0011_auto_20200818_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgue',
            name='emplacement',
            field=models.CharField(blank=True, choices=[('sol', 'Au sol'), ('tribune', 'En tribune')], max_length=20, null=True, verbose_name='Emplacement'),
        ),
    ]
