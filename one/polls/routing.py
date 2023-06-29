from django.urls import path, re_path
from polls import consumers
urlpatterns = [
    re_path(r'^ws/task_status/(?P<task_id>[^/]+)/$', consumers.TaskStatusConsumer.as_asgi()),
]