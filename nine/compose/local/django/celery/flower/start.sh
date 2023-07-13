#!/bin/bash

set -o errexit
set -o nounset

worker_ready(){
celery -A nine inspect ping
}

until worker_ready; do
    >&2 echo "Waiting for worker to become available"
    sleep 1
done
>&2 echo "Worker Ready."

celery -A nine --broker="${CELERY_BROKER}" flower

