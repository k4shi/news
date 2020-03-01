FROM python:3.6

ENV PYTHONUNBUFFERED 1

WORKDIR /opt/news

COPY ./requirements .

RUN pip3 install --no-cache-dir -r dev.txt

COPY ./docker/app/launch.sh /bin/

CMD [ "/bin/launch.sh" ]
