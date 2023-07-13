#!/bin/bash

set -o nounset
set -o errexit

worker_ready(){
    celery -A xis inspect ping
}

until worker_ready; do
    >&2 echo "Waiting for a worker to become available"
done
>&2 echo "Worker is available"

celery -A xis --broker="${CELERY_BROKER}" flower