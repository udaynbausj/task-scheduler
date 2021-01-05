from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def health(req):
    return Response(data={
        "msg": "everything is alright"
    }, status=status.HTTP_200_OK)
