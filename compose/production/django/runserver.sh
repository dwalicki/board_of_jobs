#!/bin/sh

python manage.py migrate
uvicorn config.wsgi:application --host 0.0.0.0 --port 80
