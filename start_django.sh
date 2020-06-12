#!/bin/bash

## Change the following path to suit your Django installation
cd /d/data/dd_projects/django_api;


x=`ps -ef | grep -i django | grep -v grep | grep runserver | wc -l`

if [ "$x" -lt "1" ]
then
## Change the following to suit your Django installation
### Change 0.0.0.0:8000 to suit your listening IP and port
### Change django.log to your logfile location. Using this default is a bad idea.
  ./venv/bin/python manage.py runserver 0.0.0.0:8000 2>&1 | tee -a django.log &
fi

