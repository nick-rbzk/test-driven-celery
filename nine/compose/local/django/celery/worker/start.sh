#!/bin/bash


set -o errexit
set -o nounset


celery -A nine worker -l INFO