# Installation :

Installer python 3.4+
Installer les librairies listées dans le fichier `requirements.txt`.
Créer un fichier `project/settings/dev.py` inspiré de `project/settings/dev.example.py` avec les settings de dev.

```
pip install -r requirements.txt
```
Lancer les commandes suivantes :  
 
```shell script
python manage.py makemigrations
python manage.py migrate
python manage.py init_groups
python manage.py init_config
python manage.py import_data
python manage.py createsuperuser
python manage.py runserver
```

Certaines données sont mises en cache pour améliorer la perfomance des requêtes.
Pour forcer le recalcul des "résumés clavier" il faut lancer la commande : 
```shell script
python manage.py calcul_resume_composition
```  
Normalement le résumé clavier est recalculé automatiquement à chaque modification de la composition d'un orgue.

Pour récupérer les configs depuis le site inventaire des orgues (Facteurs, types de jeux, types de claviers et )
Téléchargez le fichier config.json depuis l'url du site : https://inventaire-des-orgues.fr/api/v1/config.json
et lancer la commande suivante :

```shell script
python manage.py init_config --delete path/ver/config.json
```

l'option --delete permet de vider la base préalablement si nécessaire

# Installation du moteur de recherche 

Suivre la documentation pour installer meilisearch : 

[https://docs.meilisearch.com/](https://docs.meilisearch.com/)

Pour Windows, le script d'installation via curl ne fonctionnera pas, mais un binaire existe ici :
https://github.com/meilisearch/MeiliSearch/releases

Configurer l'url de meilisearch dans `project/settings/dev.py`, normalement : 

```python
MEILISEARCH_URL = 'http://127.0.0.1:7700'
MEILISEARCH_KEY = ''
```

Puis lancer la tache de création de l'index : 

```shell script
python manage.py build_meilisearch_index
```

Un signal django récupère les modifications d'orgues faites directement via l'interface et met à jour l'index de recherche meilisearch.
Ce signal ne récupère pas les modifications faites en ligne de commande, les modifications groupées via l'admin ou encore
les suppressions d'orgues. 
Pour mettre à jour l'index de recherche après ces types de modifications, il faut lancer la commande `build_meilisearch_index`.
En production cette commande est lancée toutes les nuits (à 2 h) pour garantir que l'index soit à jour. 

Si l'installation de meilisearch ne fonctionne pas, on peut utiliser un moteur de recherche dégradé en paramétrant : 

```python
MEILISEARCH_URL = False
```

# Faire un import de données sur le serveur : 


Placer le fichier JSON d'importation quelque part sur le disque. (s'inspirer du format de `exemple_orgue-v3.json`) 
A noter : la colonne `codification` est utilisée comme pivot pour retrouver des orgues potentiellement déjà existants dans la base de données avant
de les mettre à jour.  

Lancer :

```shell script
source /var/www/pythonenv/bin/activate
cd /var/www/portail
python manage.py import_data chemin/vers/exemple_orgue-v3.json
```

Optionel : ajouter `--delete` pour supprimer les orgues existants avant l'importation

# Travailler directement sur la base de données

```python
source /var/www/pythonenv/bin/activate
cd /var/www/portail
python manage.py shell

from orgues.models import Orgue
Orgue.objects.all()
Orgue.objects.filter(departement="Ardennes")
```

Se référer à la [documentation Django](https://docs.djangoproject.com/fr/3.1/topics/db/queries/) pour des requêtes plus poussées, avec usage notamment des commandes comme :
`exclude()`, `get()` et des suffixes : `__startwith`, `__lte`, etc.
`update()` permet les mises à jour simultanées.
Exemple : corriger les noms erronés du champ ancienne_commune :

```python
Orgue.objects.filter(ancienne_commune="/").update(ancienne_commune="")
```

# Renouveler manuellement le certificat

```python
sudo service nginx stop
sudo certbot renew
sudo service nginx start
```

# Export CSV

Bien pratique pour travailler sur un tableur type OpenOffice ou Excel...
https://inventaire-des-orgues.fr/orgues/csv

# Renouvellement des certificats

Via un fichier cron. Pour le voir :
```shell
sudo su
crontab -l
```

Commandes correspondantes :
```shell
service nginx stop
certbot renew
service nginx start
```

# Rétablir les permissions sur les fichiers

sudo chown -R fabdev:www-data /var/www/portail/static/media

# Création d'un diagramme UML à partir du modèle de données Django

Installer si nécessaire django-extensions et pydotplus (toutefois ces deux modules sont dans `requirements.txt`, donc l'installation n'est normalement pas nécessaire).

Créer un fichier de graphe (.dot) à l'aide de :
```python
python manage.py graph_models orgues -a -g > orgue.dot
```

Puis générer un diagramme .svg (ou .png) en ligne :
https://dreampuf.github.io/GraphvizOnline

# Api : 
[Voir la documentation](https://docs.inventaire-des-orgues.fr/api)

# Pense-bête Python

Pour installer un fichier Wheel depuis la console Python.
```python
import pip
from pip._internal import main as pipmain
pipmain(['install', "Chemin\\vers\\fichier.whl"])
```
