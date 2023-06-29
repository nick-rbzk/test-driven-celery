import shlex
import sys
import subprocess
from typing import Any, Optional

from django.core.management.base import BaseCommand
from django.utils import autoreload

def restart_celery():
    celery_worker_cmd = 'celery -A one worker'
    cmd = f'pkill -f "{celery_worker_cmd}"'
    subprocess.call(shlex.split(cmd))
    subprocess.call(shlex.split(f"{celery_worker_cmd} --loglevel=info")) 


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        print("Starting Celery worker with reload")
        autoreload.run_with_reloader(restart_celery)