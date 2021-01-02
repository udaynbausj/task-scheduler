from rest_framework.response import Response
from . import tasks
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def invoke_streak_cron(request):
    for i in range(2):
        tasks.invalidate_streaks.delay(i)
    return Response(data={
        "msg": "cron succeeded"
    })


@api_view(['GET'])
def streak_health(request):
    tasks.health.delay()
    return Response(data={
        "msg": "health check request is sent. results awaited. max of 5 secs."
    })
