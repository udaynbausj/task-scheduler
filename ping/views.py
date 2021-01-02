from rest_framework.response import Response
from . import tasks
from rest_framework.decorators import api_view


@api_view(['GET'])
def ping_url():
    tasks.status_check()
    return Response(data="status will be served in sometime.")
