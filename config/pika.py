from os import environ
import pika
from .settings.base import env

# "amqp://pepe:pepe@0. 0.0.0:5672/"
params = pika.URLParameters(env("RABBIT_MQ_HOST"))

connection = pika.BlockingConnection(params)

channel = connection.channel()
