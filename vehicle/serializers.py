# -*- coding:utf-8 -*-

from rest_framework import serializers
from models import Bus, BusData, MileageData
from django.apps import apps
from django.utils import timezone
from services import busStorage
from beacon.services import checkinStorage


# Serializer for terminal api
class TapiSerializer(serializers.Serializer):

    CarID = serializers.CharField()
    CarTMileage = serializers.FloatField(required=False, allow_null=True)
    CarFMileage = serializers.FloatField(required=False, allow_null=True)
    CarXMileage = serializers.FloatField(required=False, allow_null=True)
    CarStatus = serializers.IntegerField(required=False, allow_null=True, min_value=0, max_value=4)
    CarRBatteryStatus = serializers.IntegerField(required=False, allow_null=True, min_value=0, max_value=2)
    CarH2Left = serializers.FloatField(required=False, allow_null=True, min_value=0, max_value=100)
    CarH2Tmp = serializers.FloatField(required=False, allow_null=True)
    CarDBatteryStatus = serializers.IntegerField(required=False, allow_null=True, min_value=0, max_value=2)
    CarDBatteryLeft = serializers.FloatField(required=False, allow_null=True)
    CarDBatteryTmp = serializers.FloatField(required=False, allow_null=True)
    CarSpeed = serializers.FloatField(required=False, allow_null=True)
    CarGeal = serializers.IntegerField(required=False, allow_null=True, min_value=0, max_value=2)
    CarFault = serializers.IntegerField(required=False, allow_null=True, min_value=0, max_value=2)
    CarRpm = serializers.FloatField(required=False, allow_null=True)
    CarTorque = serializers.FloatField(required=False, allow_null=True)
    CarVoltage = serializers.FloatField(required=False, allow_null=True)
    CarCurrent = serializers.FloatField(required=False, allow_null=True)
    CarTmp = serializers.FloatField(required=False, allow_null=True)
    CarRBatteryVoltage = serializers.FloatField(required=False, allow_null=True)
    CarRBatteryCurrent = serializers.FloatField(required=False, allow_null=True)
    CarRBatteryTmp = serializers.FloatField(required=False, allow_null=True)
    CarDBatteryVoltage = serializers.FloatField(required=False, allow_null=True)
    CarDBatteryCurrent = serializers.FloatField(required=False, allow_null=True)
    CarLng = serializers.FloatField(required=False, allow_null=True)
    CarLat = serializers.FloatField(required=False, allow_null=True)
    CarCarbon = serializers.FloatField(required=False, allow_null=True)
    CarEnergy = serializers.FloatField(required=False, allow_null=True)
    CarSum = serializers.FloatField(required=False, allow_null=True)

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
        ret = self.process_data(validated_data)
        # print(ret)
        bid = validated_data['CarID']
        try:
            bus = Bus.objects.get(bid=bid)
        except Exception:
            bus = Bus.objects.create(bid=bid)

        cache_obj = busStorage.get(bid)
        # print(cache_obj)

        now = timezone.now()
        for modelName, objs in ret.items():
            if modelName == 'Bus':
                continue

            # update cache obj
            if modelName == 'EnergySavingData':
                checkinStorage.publish_busdata(bid, objs)
                old = cache_obj.get(modelName, {})
                for key, value in objs.items():
                    objs[key] = old.get(key, 0) + value
            cache_obj[modelName].update(objs)
            cache_obj[modelName]['timestamp'] = now

            model = apps.get_model(app_label='vehicle', model_name=modelName)
            objs['bus'] = bus
            objs['timestamp'] = now
            model.objects.create(**objs)

        # print(cache_obj)
        busStorage.set(bid, cache_obj)
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



class BusDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusData


class MileageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MileageData


class BusSerializer(serializers.ModelSerializer):
    # busdata = BusDataSerializer(read_only=True)

    class Meta:
        model = Bus
        fields = ('bid', 'plate_number', )

    # def update(self, instance, validated_data):
    #     instance.busdata = validated_data['busdata']
    #     return instance
