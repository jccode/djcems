# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


# Create your models here.
class UserProfile(models.Model):
    GENDER = (
        (1, '男'),
        (2, '女'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_regex = RegexValidator(regex=r'^\d{11}$', message="phone number must be 11 digits")
    phone = models.CharField(max_length=20, validators=[phone_regex])
    gender = models.IntegerField(choices=GENDER, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    avatar = models.ImageField(upload_to="avatar", blank=True, null=True)


def assure_user_profile_exist(pk):
    user = User.objects.get(pk=pk)
    try:
        userpofile = user.userprofile
    except UserProfile.DoesNotExist, e:
        userpofile = UserProfile(user=user)
        userpofile.save()
    return


def create_user_profile_and_token(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        # make sure username is telphone number
        up = UserProfile(user=user)
        up.save()
        Token.objects.create(user=user)


# singals
post_save.connect(create_user_profile_and_token, sender=User)
