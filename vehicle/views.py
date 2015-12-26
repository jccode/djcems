# -*- coding: utf-8 -*-

from rest_framework.decorators import api_view
from rest_framework.response import Response
from services import busStorage

# Create your views here.

@api_view(['GET'])
def busData(request, bid):
    data = busStorage.get(bid)
    return Response(data)
