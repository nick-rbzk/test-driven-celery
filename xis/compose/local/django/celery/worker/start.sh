#!/bin/bash

set -o errexit
set -o nounset

celery -A xis worker -l INFO