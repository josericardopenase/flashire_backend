from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def rabbit_test(request):
    # implementar envio a rabbit mq de procesado
    return Response({"information": "success"})
