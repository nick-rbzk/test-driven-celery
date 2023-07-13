#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python manage.py migrate
# python manage.py collectstatic --noinput
# python manage.py runserver 0.0.0.0:8000
daphne -e ssl:443:privateKey=./certs/apache-selfsigned.key:certKey=./certs/apache-selfsigned.crt -u /tmp/daphne.sock -p 8080 five.asgi:application -b 0.0.0.0