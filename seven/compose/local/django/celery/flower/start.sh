#!/bin/bash

set -o errexit
set -o nounset


worker_ready(){
    celery -A seven inspect ping
}

until worker_ready; do
    >&2 echo "Celery worker is NOT available"
    sleep 1
done
>&2 echo "Celery worker AVAILABLE"


celery -A seven --broker="${CELERY_BROKER}" flower