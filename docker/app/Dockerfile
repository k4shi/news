FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV DJANGO_CONFIGURATION Dev
ENV DJANGO_SETTINGS_MODULE backend.settings

WORKDIR /opt/backend

COPY ./requirements .

RUN pip3 install --no-cache-dir -r dev.txt

COPY ./docker/app/launch.sh /bin/

CMD [ "/bin/launch.sh" ]
