#!/bin/bash

set -o errexit
set -o nounset

worker_ready(){
    celery -A four inspect ping
}

until worker_ready; do
    >&2 echo "Celery Workers are not available"
    sleep 1
done
>&2 echo "Celery workers are AVAILABLE"

celery -A four --broker="${CELERY_BROKER}" flower