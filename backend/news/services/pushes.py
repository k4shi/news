import pika
from django.conf import settings
from protocol.python import news_pb2


def msg_pushes(msg):
    _news = news_pb2.News()
    _news.title = msg['title']

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=settings.RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=settings.RABBITMQ_TOPIC)
    channel.basic_publish(exchange='', routing_key=settings.RABBITMQ_TOPIC, body=_news.SerializeToString())
    connection.close()
    return True
