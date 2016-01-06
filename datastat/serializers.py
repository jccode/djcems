
from rest_framework import serializers
from models import UserSavingEnergyPerDay, UserSavingEnergyPerMonth

class UserSavingEnergyPerDaySerilizer(serializers.Serializer):
    class Meta:
        model = UserSavingEnergyPerDay


class UserSavingEnergyPerMonthSerilizer(serializers.Serializer):
    class Meta:
        model = UserSavingEnergyPerMonth

