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

    def create(self, validated_data):
        # password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        password = self.initial_data["password"]
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                 instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
        # write_only_fields = ('password')
        read_only_fields = ('id')



class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)

    # def create(self, validated_data):
    #     uid = validated_data.pop('uid', None)
    #     instance = self.Meta.model(**validated_data)
    #     if uid is not None:
    #         user = User.objects.get(id=uid)
    #         instance.user = user
    #         instance.save()
    #         return instance
    #     else:
    #         raise "uid is not exist"

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = UserProfile
        fields = ('user', 'phone', 'avatar', 'nickname', 'birthday', 'qq', 'wechat', 'weibo')



