# -*- coding:utf-8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

class CollectVehicleData(APIView):

    authentication_classes = (authentication.BasicAuthentication, )
    permission_classes = (permissions.IsAdminUser, )

    def post(self, request, *args, **kwargs):
        pass