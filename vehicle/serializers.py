# -*- coding:utf-8 -*-

from rest_framework import serializers
from .models import Bus
from django.apps import apps
from django.utils import timezone


class TapiSerializer(serializers.Serializer):
    CarID = serializers.CharField()
    CarTMileage = serializers.IntegerField(required=False,allow_null=True)
    CarFMileage = serializers.IntegerField(required=False,allow_null=True)
    CarXMileage = serializers.IntegerField(required=False,allow_null=True)
    CarStatus = serializers.IntegerField(required=False,allow_null=True)

    mapping = {
        "CarID": "Bus.bid",
        "CarTMileage": "MileageData.total",
        "CarFMileage": "MileageData.section",
        "CarXMileage": "MileageData.remain",
        "CarStatus": "BusData.status",
    }

    def create(self, validated_data):
        # print('------------ serializer ------------')
        # print(validated_data)
        ret = self.process_data(validated_data)
        # print(ret)
        bid = validated_data['CarID']
        try:
            bus = Bus.objects.get(bid=bid)
        except:
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
            if not self.mapping.has_key(str(reqKey)):
                continue
            target = self.mapping[str(reqKey)]
            [model, field] = target.split(".")
            if not result.has_key(model):
                result[model] = {}
            result[model][field] = value
        return result

