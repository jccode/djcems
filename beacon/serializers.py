# -*- coding: utf-8 -*-

from rest_framework import serializers
from models import Beacon, BeaconCheckIn
from vehicle.serializers import BusSerializer


class BeaconSerializer(serializers.ModelSerializer):
    stick_on = BusSerializer(many=True, read_only=True)

    class Meta:
        model = Beacon


# class BeaconCheckInSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BeaconCheckIn

class BeaconCheckinSerializer(serializers.Serializer):
    EVENT = (
        (0, "enter"),
        (1, "leave"),
        (2, "stay"),
    )
    uid = serializers.IntegerField()
    bid = serializers.CharField(max_length=45)
    event = serializers.ChoiceField(choices=EVENT)
    timestamp = serializers.DateTimeField()