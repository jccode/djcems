# -*- coding:utf-8 -*-

from rest_framework import serializers
from .models import Bus
from django.apps import apps
from django.utils import timezone


class TapiSerializer(serializers.Serializer):

    CarID = serializers.CharField()
    CarTMileage = serializers.IntegerField(required=False, allow_null=True)
    CarFMileage = serializers.IntegerField(required=False, allow_null=True)
    CarXMileage = serializers.IntegerField(required=False, allow_null=True)
    CarStatus = serializers.IntegerField(required=False, allow_null=True)
    CarRBatteryStatus = serializers.IntegerField(required=False, allow_null=True)
    CarH2Left = serializers.IntegerField(required=False, allow_null=True)
    CarH2Tmp = serializers.IntegerField(required=False, allow_null=True)
    CarDBatteryStatus = serializers.IntegerField(required=False, allow_null=True)
    CarDBatteryLeft = serializers.IntegerField(required=False, allow_null=True)
    CarDBatteryTmp = serializers.IntegerField(required=False, allow_null=True)
    CarSpeed = serializers.IntegerField(required=False, allow_null=True)
    CarGeal = serializers.IntegerField(required=False, allow_null=True)
    CarFault = serializers.IntegerField(required=False, allow_null=True)
    CarRpm = serializers.IntegerField(required=False, allow_null=True)
    CarTorque = serializers.IntegerField(required=False, allow_null=True)
    CarVoltage = serializers.IntegerField(required=False, allow_null=True)
    CarCurrent = serializers.IntegerField(required=False, allow_null=True)
    CarTmp = serializers.IntegerField(required=False, allow_null=True)
    CarRBatteryVoltage = serializers.IntegerField(required=False, allow_null=True)
    CarRBatteryCurrent = serializers.IntegerField(required=False, allow_null=True)
    CarRBatteryTmp = serializers.IntegerField(required=False, allow_null=True)
    CarDBatteryVoltage = serializers.IntegerField(required=False, allow_null=True)
    CarDBatteryCurrent = serializers.IntegerField(required=False, allow_null=True)
    CarLng = serializers.FloatField(required=False, allow_null=True)
    CarLat = serializers.FloatField(required=False, allow_null=True)
    CarCarbon = serializers.IntegerField(required=False, allow_null=True)
    CarEnergy = serializers.IntegerField(required=False, allow_null=True)
    CarSum = serializers.IntegerField(required=False, allow_null=True)

    mapping = {
        "CarID": "Bus.bid",
        "CarTMileage": "MileageData.total",
        "CarFMileage": "MileageData.section",
        "CarXMileage": "MileageData.remain",
        "CarStatus": "BusData.status",
        "CarRBatteryStatus": "FuelCellData.status",
        "CarH2Left": "GasData.remain",
        "CarH2Tmp": "GasData.bottle_temp",
        "CarDBatteryStatus": "PowerBatteryData.status",
        "CarDBatteryLeft": "PowerBatteryData.remain",
        "CarDBatteryTmp": "PowerBatteryData.temp",
        "CarSpeed": "BusData.speed",
        "CarGeal": "BusData.gear",
        "CarFault": "BusData.failure_info",
        "CarRpm": "MotorData.speed",
        "CarTorque": "MotorData.torque",
        "CarVoltage": "MotorData.voltage",
        "CarCurrent": "MotorData.current",
        "CarTmp": "MotorData.temp",
        "CarRBatteryVoltage": "FuelCellData.voltage",
        "CarRBatteryCurrent": "FuelCellData.current",
        "CarRBatteryTmp": "FuelCellData.temp",
        "CarDBatteryVoltage": "PowerBatteryData.voltage",
        "CarDBatteryCurrent": "PowerBatteryData.current",
        "CarLng": "BusData.longitude",
        "CarLat": "BusData.latitude",
        "CarCarbon": "EnergySavingData.emission_reduction",
        "CarEnergy": "EnergySavingData.energy_saving_amount",
        "CarSum": "EnergySavingData.energy_saving_money",
    }

    def create(self, validated_data):
        # print('------------ serializer ------------')
        # print(validated_data)
        ret = self.process_data(validated_data)
        # print(ret)
        bid = validated_data['CarID']
        try:
            bus = Bus.objects.get(bid=bid)
        except Exception:
            bus = Bus.objects.create(bid=bid)

        now = timezone.now()
        for modelName, objs in ret.items():
            if modelName == 'Bus':
                continue
            model = apps.get_model(app_label='vehicle', model_name=modelName)
            objs['bus'] = bus
            objs['timestamp'] = now
            model.objects.create(**objs)
            # m = model(**objs)
            # m.save()
        return bus

    def process_data(self, reqdata):
        result = {}
        for reqKey, value in reqdata.items():
            if not str(reqKey) in self.mapping:
                continue
            target = self.mapping[str(reqKey)]
            [model, field] = target.split(".")
            if model not in result:
                result[model] = {}
            result[model][field] = value
        return result
