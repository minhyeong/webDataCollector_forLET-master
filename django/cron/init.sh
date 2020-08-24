#!/bin/sh
printenv | awk '{print "export " $1}' > /code/cron/env.sh
