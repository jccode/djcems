# -*- coding: utf-8 -*-

from rest_framework import serializers
from models import Beacon


class BeaconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beacon
