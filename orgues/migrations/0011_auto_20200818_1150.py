# Generated by Django 2.2.7 on 2020-08-18 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgues', '0010_auto_20200818_0955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orgue',
            old_name='elevation',
            new_name='emplacement',
        ),
    ]
