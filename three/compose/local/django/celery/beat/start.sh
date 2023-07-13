#!/bin/bash

set -o errexit
set -o nounset

rm -rf 'celerybet.py'
celery -A three beat -l INFO