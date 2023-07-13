#!/bin/bash
set -o errexit
set -o nounset

rm -f 'celerybeat.pid'
celery -A eight beat -l INFO
