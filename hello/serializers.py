
from rest_framework import serializers

class AddressSerializer(serializers.Serializer):
    address = serializers.CharField()
    zipcode = serializers.CharField()

class AccountSerializer(serializers.Serializer):
    name = serializers.CharField()
    address = AddressSerializer

