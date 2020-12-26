from rest_framework.response import Response
from .tasks import invalidate_streaks
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def invoke_streak_cron(request):
    for i in range(2):
        invalidate_streaks.delay(i)
    return Response(data={
        "msg": "cron succeeded"
    })
