# Generated by Django 2.2.7 on 2020-02-10 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgues', '0008_accessoire'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgue',
            name='accessoires',
            field=models.ManyToManyField(blank=True, to='orgues.Accessoire'),
        ),
    ]