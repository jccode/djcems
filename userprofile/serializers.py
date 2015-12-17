# -*- coding:utf-8 -*-

from django.contrib.auth.models import User, Group
from models import UserProfile
from rest_framework import serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'id')



class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = ('user', 'phone', 'gender', 'age', 'avatar')
