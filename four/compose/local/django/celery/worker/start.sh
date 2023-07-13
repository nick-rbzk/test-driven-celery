#!/bin/bash

set -o errexit
set -o nounset


celery -A four worker -l INFO