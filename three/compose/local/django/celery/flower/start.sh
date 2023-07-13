#!/bin/bash

set -o errexit
set -o nounset


worker_ready(){
    celery -A three inspect ping
}

until worker_ready; do
    >&2 echo "Celery workers are not available"
    sleep 1
done

>&2 echo "Celery Workers Available."

celery -A three --broker="${CELERY_BROKER}" flower