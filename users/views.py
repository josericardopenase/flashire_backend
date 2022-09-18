from rest_framework.decorators import api_view
from rest_framework.response import Response
from config.pika import channel


@api_view(["GET"])
def rabbit_test(request):
    # implementar envio a rabbit mq de procesado
    channel.basic_publish(exchange="", routing_key="admin", body="HELLOOOO WORLD")
    print("se supone que se ha enviado un esto")
    return Response({"information": "success"})
