from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'one.settings')

app = Celery('one')

# Using a string here eliminates the need to serialize 
# the configuration object to child processes by the Celery worker.

# - namespace='CELERY' means all celery-related configuration keys
app.config_from_object('django.conf:settings', namespace='CELERY')


# Load task modules from all registered Django applications.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
    
    
app.conf.beat_schedule = {
    #Scheduler Name
    'print-message-ten-seconds': {
        # Task Name (Name Specified in Decorator)
        'task': 'print_msg_main',  
        # Schedule      
        'schedule': 10.0,
        # Function Arguments 
        'args': ("Hello You Clever Bastard!",) 
    },
    #Scheduler Name
    'print-time-twenty-seconds': {
        # Task Name (Name Specified in Decorator)
        'task': 'print_time',  
        # Schedule      
        'schedule': 20.0, 
    },
    #Scheduler Name
    'calculate-forty-seconds': {
        # Task Name (Name Specified in Decorator)
        'task': 'get_calculation',  
        # Schedule      
        'schedule': 40.0,
        # Function Arguments 
        'args': (10,20) 
    },
} 
