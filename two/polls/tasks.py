from celery import shared_task
from celery.signals import task_postrun
from polls.consumers import notify_chennel_layer

import json
import random
import requests

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task(bind=True)
def task_process_notification(self):
    try:
        if not random.choice([0, 1]):
            raise Exception("test exception")
        requests.post("https://httpbin.org/delay/5")
    except Exception as e:
        logger.error("exception raised. It will be retried in 5 seconds")
        raise self.retry(exc=e, countdown=5)
            

@shared_task()
def sample_task(email):
    from polls.views import api_call
    api_call(email)

@task_postrun.connect
def task_post_run_handler(task_id, **kwargs):
    notify_chennel_layer(task_id)