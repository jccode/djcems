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
    permission_classes = (permissions.IsAdminUser, )

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
        print(request.data)

        # ret = self.process_data(request.data)
        #
        # print(ret)
        # bid = ret['Bus']['bid']
        #
        # try:
        #     bus = Bus.objects.get(bid=bid)
        # except:
        #     bus = Bus.objects.create(bid=bid)
        # for modelName, objs in ret.items():
        #     if modelName == 'Bus':
        #         continue
        #     model = apps.get_model(app_label='vehicle', model_name=modelName)
        #     # model.objects.create(*objs)
        #     m = model(*objs)
        #     m.save()

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
