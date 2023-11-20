import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings.dev')
#setting this Enviroment Variable to the storefront.settings

celery = Celery('storefront')
celery.config_from_object('django.conf:settings', namespace='CELERY')
# we going to "django.conf and loading Settings"
# namespace'CELERY' means, In settings.py all of our config will starts from 'CELERY'

celery.autodiscover_tasks()
# automatically discover tasks from tasks folder