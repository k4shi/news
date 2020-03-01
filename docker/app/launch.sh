#!/bin/bash

cd /opt/news

if [ ! -f "$ENV_FILE" ]; then
   cp example.env .env
fi

echo "Apply database migrations"
python3 manage.py migrate

echo "Collect static files"
yes yes | python3 manage.py collectstatic

echo "Starting server"
uwsgi --ini /opt/news/configs/uwsgi.docker.ini
