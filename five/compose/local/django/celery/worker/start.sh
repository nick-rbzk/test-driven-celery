#!/bin/bash

set -o errexit 
set -o nounset

celery -A five worker -l INFO