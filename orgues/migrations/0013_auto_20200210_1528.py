# Generated by Django 2.2.7 on 2020-02-10 15:28

from django.db import migrations, models
import orgues.models


class Migration(migrations.Migration):

    dependencies = [
        ('orgues', '0012_auto_20200210_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='clavier',
            name='etendue',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[orgues.models.validate_etendue]),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='commentaire_tuyauterie',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='sommiers',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orgue',
            name='soufflerie',
            field=models.TextField(blank=True, null=True),
        ),
    ]