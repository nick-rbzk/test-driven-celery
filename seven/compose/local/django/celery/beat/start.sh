#!/bin/bash

set -o errexit
set -o nounset


rm -f 'celerybeat.pid'
celery -A seven beat -l INFO