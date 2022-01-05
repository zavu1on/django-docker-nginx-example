#!/usr/bin/env sh

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input

exec gunicorn DockerWeb.wsgi:application -b 0.0.0.0:8000 -w 4
