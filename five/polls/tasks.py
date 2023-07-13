from celery import shared_task
from celery.signals import task_postrun
import random
import requests
from celery.utils.log import get_task_logger
from polls.consumers import notify_channel_layer

logger = get_task_logger(__name__)


@shared_task()
def sample_task(email):
    print(email)
    print("Sample task")
    from polls.views import api_call
    api_call(email)

@shared_task(bind=True)
def task_process_notification(self):
    try:
        if not random.choice([0, 1]):
            raise Exception("task process notifcation")
        
        requests.post("https://httpbin.org/delay/5")
    except Exception as e:
        logger.error("exception raised, it would retry after 5 seconds")

@task_postrun.connect
def task_postrun_handler(task_id, **kwargs):
    notify_channel_layer(task_id)



