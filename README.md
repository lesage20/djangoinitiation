
# django initiation
`python3`, `python3-django`
pour commencer il faut créer un environnement virtuel avec:
python3 -m venv venv

ensuite il faut activer l'environnement virtuel avec:
source venv/bin/activate

on installe django avec la commande:
pip install django == 'version souhaitée'

on crée un nouvo projet avec la commande:
django-admin startproject 'nom du projet'

on lance le projet avec la commande:
python manage.py runserver

on fait la migration avec la commande:
python manage.py migrate

on crée un nouvel utilisateur avec la commande:
python manage.py createsuperuser


