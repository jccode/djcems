# -*- coding: utf-8 -*-

from rest_framework import serializers
from models import Beacon, BeaconCheckIn
from vehicle.serializers import BusSerializer


class BeaconSerializer(serializers.ModelSerializer):
    stick_on = BusSerializer(many=True, read_only=True)

    class Meta:
        model = Beacon


class BeaconCheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeaconCheckIn