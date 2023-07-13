#!/bin/bash

set -o errexit
set -o nounset

rm -f 'celerybeat.pid'
celery -A nine beat -l INFO
