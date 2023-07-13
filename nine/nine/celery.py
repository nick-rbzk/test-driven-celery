from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nine.settings")

celery = Celery('nine')
celery.autodiscover_tasks()
celery.config_from_object("django.conf:settings", namespace="CELERY")