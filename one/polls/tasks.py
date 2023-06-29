import random
import requests
import json

from celery import shared_task
from celery.signals import task_postrun
from celery.utils.log import get_task_logger

from polls.consumers import notify_channel_layer
logger = get_task_logger(__name__)


@shared_task(name="api_call")
def sample_task(email, *args,**kwargs):
    from polls.views import api_call
    api_call(email)
    
@shared_task(bind=True)
def task_process_notification(self):
    try:
        # if not random.choice([0,1]):
            # raise Exception()
        print("PROCESS NOTIFICATION")
        requests.post('http://httpbin.org/delay/5') 
    
    except Exception as e:
        print(str(e))
        raise self.retry(exc=e, countdown=5)


@task_postrun.connect
def task_postrun_handler(task_id, **kwargs):
    notify_channel_layer(task_id)
