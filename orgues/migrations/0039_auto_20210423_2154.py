# Generated by Django 3.1.7 on 2021-04-23 21:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orgues', '0038_auto_20210414_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='facteur',
            name='updated_by_user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='clavier',
            name='commentaire',
            field=models.CharField(blank=True, help_text='Particularités specifiques du clavier (transmission, ', max_length=200, null=True),
        ),
    ]
