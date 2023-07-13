#!/bin/bash


set -o errexit
set -o nounset
set -o pipefail


postgres_ready(){
python << END

import sys
import psycopg2

try:
    psycopg2.connect(
        dbname="${SQL_DATABASE}",
        user="${SQL_USER}",
        password="${SQL_PASSWORD}",
        host="${SQL_HOST}",
        port="${SQL_PORT}",
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)

END
}

until postgres_ready; do
    >&2 echo "Waiting or POSTGRESQL to become available."
    sleep 1
done
>&2 echo "POSTGRESQL is AVAILABLE."


exec "$@"