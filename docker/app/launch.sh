#!/bin/bash

cd /opt/backend

if [ ! -f "$ENV_FILE" ]; then
   cp example.env .env
fi

echo "Apply database migrations"
python3 manage.py migrate

echo "Collect static files"
yes yes | python3 manage.py collectstatic

echo "Starting server"
uwsgi --ini /opt/backend/configs/uwsgi.docker.ini
