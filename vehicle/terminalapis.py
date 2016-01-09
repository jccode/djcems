# -*- coding:utf-8 -*-
# terminal api

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status
import logging
from .models import Bus
from .serializers import TapiSerializer


logger = logging.getLogger(__name__)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class CollectVehicleData(APIView):

    authentication_classes = (authentication.BasicAuthentication, )
    permission_classes = (permissions.AllowAny,)  # (permissions.DjangoModelPermissions, )
    queryset = Bus.objects.all()

    # def get(self, request, *args, **kwargs):
    #     return Response(True)

    def post(self, request, *args, **kwargs):
        """
        terminal api

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ip = get_client_ip(request)
        logger.debug("[receive data from terminal.][" + str(request.data) + "]", extra={"clientip":ip})

        serializer = TapiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response(True)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
