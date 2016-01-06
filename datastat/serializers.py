
from rest_framework import serializers
from models import UserSavingEnergyPerDay, UserSavingEnergyPerMonth

class UserSavingEnergyPerDaySerilizer(serializers.ModelSerializer):
    class Meta:
        model = UserSavingEnergyPerDay


class UserSavingEnergyPerMonthSerilizer(serializers.ModelSerializer):
    class Meta:
        model = UserSavingEnergyPerMonth

