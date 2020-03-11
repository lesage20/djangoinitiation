
# django initiation
`python3` <br>
pour commencer il faut créer un environnement virtuel avec: <br>
`python3 -m venv venv`

ensuite il faut activer l'environnement virtuel avec:<br>
`source venv/bin/activate`

on installe django avec la commande: <br>
`pip install django == 'version souhaitée'`

on crée un nouvo projet avec la commande: <br>
`django-admin startproject 'nom du projet'`

on lance le projet avec la commande: <br>
`python manage.py runserver`

on fait la migration avec la commande: <br>
`python manage.py migrate`

on crée un nouvel utilisateur avec la commande: <br>
`python manage.py createsuperuser`


in settings.py of project

  STATIC_URL = '/static/'
  MEDIA_URL = '/media/'
  STATICFILES_DIRS = [
      os.path.join(BASE_DIR,'static')
  ]
  STATIC_ROOT= os.path.join(BASE_DIR, '../static_cdn')
  MEDIA_ROOT= os.path.join(BASE_DIR, '../media_cdn')

in urls.py of project

  from django.conf import settings
  from django.conf.urls.static import static
  
  
  
  
  
  
  if settings.DEBUG :
      urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
      urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)


