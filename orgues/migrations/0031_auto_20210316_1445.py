# Generated by Django 2.2.13 on 2021-03-16 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgues', '0030_auto_20210312_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgue',
            name='proprietaire',
            field=models.CharField(choices=[('commune', 'Commune'), ('etat', 'Etat'), ('association_culturelle', 'Association culturelle'), ('diocese', 'Diocèse'), ('paroisse', 'Paroisse'), ('congregation', 'Congrégation'), ('etablissement_scolaire', 'Etablissement scolaire'), ('conservatoire', 'Conservatoire ou Ecole de musique'), ('hopital', 'Hôpital')], default='commune', max_length=40, null=True, verbose_name='Propriétaire'),
        ),
    ]