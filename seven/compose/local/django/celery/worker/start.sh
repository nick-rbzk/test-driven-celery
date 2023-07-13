#!/bin/bash

set -o errexit
set -o nounset


celery -A seven worker -l INFO