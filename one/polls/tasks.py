import random
import requests
import json

from celery import shared_task, Task
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
        if not random.choice([0,1]):
            raise Exception()
        print("PROCESS NOTIFICATION")
        requests.post('http://httpbin.org/delay/5') 
    
    except Exception as e:
        print(str(e))
        logger.error("exception raise it would retry after 5 sec")
        raise self.retry(exc=e, countdown=5)

@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5})
def task_process_notification2(self):
    if not random.choice([0,1]):
        raise Exception()
    print("Process notification 2")
    requests.post('http://httpbin.org/delay/5') 

@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=5, retry_jitter=True, retry_kwargs={"max_retries":5})
def task_process_notification3(self):
    if not random.choice([0, 1]):
        raise Exception()
    print("PROCESS NOTIFICATION 3")
    requests.post('http://httpbin.org/delay/5') 

class BaseTaskWithRetry(Task):
    autoretry_for=(Exception, KeyError)
    retry_kwargs={"max_retries": 5}
    retry_backoff=True

@shared_task(bind=True, base=BaseTaskWithRetry)
def task_process_notification4():
    if not random.choice([0,1]):
        raise Exception()
    print("PROCESS NOTIFICATION 4")
    requests.post('http://httpbin.org/delay/5') 
    


@task_postrun.connect
def task_postrun_handler(task_id, **kwargs):
    notify_channel_layer(task_id)


@shared_task(name="default:dynamic_example_one")
def dynamic_example_one():
    logger.info("Example One")
    print("Example ONe")


@shared_task(name="low_priority:dynamic_example_two")
def dynamic_example_two():
    logger.info("Example two")
    print("Example two")


@shared_task(name="high_priority:dynamic_example_three")
def dynamic_example_three():
    logger.info("Example three")
    print("Example three")