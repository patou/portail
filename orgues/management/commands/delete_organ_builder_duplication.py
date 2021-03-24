import os
import json
from django.core.management.base import BaseCommand
from orgues.models import Facteur
from tqdm import tqdm
from django.db.models import Count

class Command(BaseCommand):
    help = "Modifie la longitude et la latitude des ateliers des facteurs d'orgue"

    def handle(self, *args, **options):
        print(Facteur.objects.values('nom').annotate(nom_count=Count('nom')).filter(nom_count__gt=1))
        doublons = Facteur.objects.values('nom').annotate(nom_count=Count('nom')).filter(nom_count__gt=1)
        for doublon in doublons:
            facteurs = Facteur.objects.filter(nom=doublon['nom'])
            facteur_quon_garde = facteurs[0]
            facteurs_qui_disparaissent = facteurs[1:]
            for facteur_qui_disparait in facteurs_qui_disparaissent:
                for evenement in Evenement.objects.filter(facteurs=facteur_qui_disparait):
                    evenement.facteurs.remove(facteur_qui_disparait)
                    evenement.facteurs.add(facteur_quon_garde)
                    evenement.save()
                orgues = Orgue.objects.filter(entretien=facteur_qui_disparait)
                for orgue in orgues:
                    orgue.entretien.remove(facteur_qui_disparait)
                    orgue.entretien.add(facteur_quon_garde)
                    orgue.save()
                print("Le doublon du facteur {} a été corrigé.")
                facteur_qui_disparait.delete()