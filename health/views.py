from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def health(req):
    return Response(data={
        "msg": "everything is alright"
    })
