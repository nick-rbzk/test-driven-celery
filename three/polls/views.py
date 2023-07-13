import json
import random
import requests

from django.shortcuts import render
from celery.result import AsyncResult
from celery.utils.log import get_logger
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from polls.forms import YourForm
from polls.tasks import sample_task, task_process_notification

logger = get_logger(__name__)
def api_call(email):
    if random.choice([0,1]):
        pass
        # raise Exception("random operational exception")
    
    requests.post("https://httpbin.org/delay/5")
    
    
def subscribe(request):
    if request == "POST":
        form = YourForm(request.POST)
        if form.is_valid():
            task = sample_task.delay(form.cleaned_data['email'])
            return JsonResponse({
                "task_id": task.task_id
            })
    form = YourForm()
    return render(request, 'form.html', {"form": form})


def task_status(request):
    task_id = request.POST.get("task_id")
    
    if task_id:
        task = AsyncResult(task_id)
        state = task.state
        
        if state == "FAILURE":
            error = str(task.result)
            response = {
                "state": state,
                "error": error
            }
        else:
            response = {
                "state": state,
            }
        return JsonResponse(response)

@csrf_exempt
def webhook_test(request):
   if not random.choice([0, 1]):
       raise Exception()
   
   requests.post("https://httpbin.org/delay/5")
   return HttpResponse('pong')

@csrf_exempt
def webhook_test_async(request):
    task = task_process_notification.delay()
    logger.info(task.id)
    return HttpResponse('pong')

def subscribe_ws(request):
    if request.method == "POST":
        form = YourForm(request.POST)
        if form.is_valid():
            task = sample_task.delay(form.cleaned_data['email'])
            return JsonResponse({
                'task_id': task.task_id
            })
    
    form = YourForm()
    return render(request, 'form_ws.html', {"form": form})