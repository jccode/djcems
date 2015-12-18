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


class CollectVehicleData(APIView):

    authentication_classes = (authentication.BasicAuthentication, )
    permission_classes = (permissions.DjangoModelPermissions, )
    queryset = Bus.objects.all()

    # mapping = {
    #     "CarID": "Bus.bid",
    #     "CarTMileage": "MileageData.total",
    #     "CarFMileage": "MileageData.section",
    #     "CarXMileage": "MileageData.remain",
    #     "CarStatus": "BusData.status",
    #     "CarRBatteryStatus": "FuelCellData.status",
    #     "CarH2Left": "GasData.remain",
    #     "CarH2Tmp": "GasData.bottle_temp",
    #     "CarDBatteryStatus": "PowerBatteryData.status",
    #     "CarDBatteryLeft": "PowerBatteryData.remain",
    #     "CarDBatteryTmp": "PowerBatteryData.temp",
    #     "CarSpeed": "BusData.speed",
    #     "CarGeal": "BusData.gear",
    #     "CarFault": "BusData.failure_info",
    #     "CarRpm": "MotorData.speed",
    #     "CarTorque": "MotorData.torque",
    #     "CarVoltage": "MotorData.voltage",
    #     "CarCurrent": "MotorData.current",
    #     "CarTmp": "MotorData.temp",
    #     "CarRBatteryVoltage": "FuelCellData.voltage",
    #     "CarRBatteryCurrent": "FuelCellData.current",
    #     "CarRBatteryTmp": "FuelCellData.temp",
    #     "CarDBatteryVoltage": "PowerBatteryData.voltage",
    #     "CarDBatteryCurrent": "PowerBatteryData.current",
    #     "CarLng": "BusData.longitude",
    #     "CarLat": "BusData.latitude",
    #     "CarCarbon": "EnergySavingData.emission_reduction",
    #     "CarEnergy": "EnergySavingData.energy_saving_amount",
    #     "CarSum": "EnergySavingData.energy_saving_money",
    # }

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
        logger.debug(" ------------ CALLING TERMINAL API ----------------")
        logger.debug(request.data)

        serializer = TapiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response(True)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def process_data(self, reqdata):
    #     result = {}
    #     for reqKey, value in reqdata.items():
    #         if not self.mapping.has_key(str(reqKey)):
    #             continue
    #         target = self.mapping[str(reqKey)]
    #         [model, field] = target.split(".")
    #         if not result.has_key(model):
    #             result[model] = []
    #         result[model].append((field, value))
    #     return result
