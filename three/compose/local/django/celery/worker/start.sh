#!/bin/bash

set -o errexit
set -o nounset


celery -A three worker -l INFO