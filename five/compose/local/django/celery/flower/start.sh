#!/bin/bash

set -o errexit
set -o nounset

worker_ready(){
    celery -A five inspect ping
}

until worker_ready; do
    >&2 echo "Waiting for the worker to become available"
done

>&2 echo "Worker is AVAILABLE."

celery -A five --broker="${CELERY_BROKER}" flower