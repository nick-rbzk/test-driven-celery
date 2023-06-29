from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'two.settings')

app = Celery('two')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
