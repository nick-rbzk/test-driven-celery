#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

python manage.py migrate
python manage.py collectstatic --noinput
# python manage.py runserver 0.0.0.0:8000
daphne -e ssl:443:privateKey=./certs/apache-selfsigned.key:certKey=./certs/apache-selfsigned.crt -u /tmp/daphne.sock -p 8000 four.asgi:application -b 0.0.0.0
