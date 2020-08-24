#!/bin/sh
. /code/cron/env.sh

python /code/manage.py dumpdata --exclude auth.permission --exclude contenttypes > /backup/dump_$(date +\%Y\%m\%d\%H\%M).json
