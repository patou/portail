# Generated by Django 3.1.7 on 2021-03-23 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['order', 'created_date']},
        ),
    ]
