#!/bin/bash

set -o errexit
set -o nounset

celery -A two worker -l INFO