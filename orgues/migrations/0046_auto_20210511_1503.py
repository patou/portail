# Generated by Django 3.1.8 on 2021-05-11 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgues', '0045_auto_20210511_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgue',
            name='code_insee',
            field=models.CharField(max_length=5, verbose_name='Code_INSEE'),
        ),
    ]