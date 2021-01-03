from rest_framework.response import Response
from . import tasks
from rest_framework.decorators import api_view


@api_view(['GET'])
def ping_url(request):
    print("ping task triggered")
    tasks.status_check.delay()
    return Response(data="status will be served in sometime.")
