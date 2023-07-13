#!/bin/bash

set -o nounset
set -o errexit
set -o pipefail


python manage.py migrate
# python manage.py runserver 0.0.0.0:8000
daphne -e ssl:443:privateKey=./certs/apache-selfsigned.key:certKey=./certs/apache-selfsigned.crt \
-u /tmp/daphne.sock \
-p 8080 nine.asgi:application \
-b 0.0.0.0

