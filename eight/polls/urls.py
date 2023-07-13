from django.urls import path
from polls.views import *

urlpatterns = [
    path("form/", subscribe, name="subscribe"),
    path("task_status/", task_status, name="task_status"),
    path("webhook_test/", webhook_test, name="webhook_test"),
    path("webhook_test_async/", webhook_test_async, name="webhook_test_async"),
    path("form_ws/", subscribe_ws, name="subscribe_ws"),
]

