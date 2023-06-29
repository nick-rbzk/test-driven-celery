#!/bin/bash

worker_ready() {
    celery -A two inspect ping
}

until worker_ready; do
    >&2 echo 'Celery worker not available'
    sleep 1
done
>&2 echo 'Celery worker available'

celery -A two --broker="${CELERY_BROKER}" flower