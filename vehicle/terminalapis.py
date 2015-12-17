# -*- coding:utf-8 -*-
# terminal api

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status
from django.apps import apps
from .apps import VehicleConfig
from .models import Bus
from .serializers import TapiSerializer

class CollectVehicleData(APIView):

    authentication_classes = (authentication.BasicAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    mapping = {
        "CarID": "Bus.bid",
        "CarTMileage": "MileageData.total",
        "CarFMileage": "MileageData.section",
        "CarXMileage": "MileageData.remain",
        "CarStatus": "BusData.status",
    }

    def get(self, request, *args, **kwargs):
        print(request.data)
        return Response(True)

    def post(self, request, *args, **kwargs):
        """
        terminal api

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        print(" ------------ CALLING TERMINAL API ----------------")
        # print(request.data)

        serializer = TapiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response(True)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def process_data(self, reqdata):
        result = {}
        for reqKey, value in reqdata.items():
            if not self.mapping.has_key(str(reqKey)):
                continue
            target = self.mapping[str(reqKey)]
            [model, field] = target.split(".")
            if not result.has_key(model):
                result[model] = []
            result[model].append((field, value))
            # result[model][field] = value
        return result
