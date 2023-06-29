from django.urls import path, include

from polls.views import subscribe, task_status, webhook_test, webhook_test_async, subscribe_ws

from polls.consumers import *
urlpatterns = [
    path('form/', subscribe, name="form"),
    path('task_status/', task_status, name="task-status"),
    path('web_hook/', webhook_test, name="webhook_test"),
    path('webhook_test_async/', webhook_test_async, name="webhook_test_async"),
    path('form_ws/', subscribe_ws, name="form_ws"),
    # path('ws/task_status/<task_id>/', TaskStatusConsumer.as_asgi()),
]
    