# -*- coding:utf-8 -*-

import logging

from django.contrib.auth.models import User, Group
from djcems.utils import rest_anonymous
from models import UserProfile
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer, UserProfileSerializer

# Create your views here.

logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


@api_view(['GET'])
def curruser(request, **kwargs):
    cuser = request.user
    # serializer = UserProfileSerializer(cuser.userprofile, context={'request': request})
    # return Response(serializer.data)

    return Response({
        'id': cuser.id,
        'username': cuser.username,
        'email': cuser.email,
        'groups': map(lambda g: g.name, cuser.groups.all()),
        'phone': cuser.userprofile.phone
    })


@api_view(['GET'])
@rest_anonymous()
def userexist(request, *args, **kwargs):
    name = request.GET.get("q", None)
    if not name:
        return Response(data="paramter q is required", status=status.HTTP_400_BAD_REQUEST)
    exist = User.objects.filter(username=name).count() > 0
    return Response(exist)


@api_view(['POST'])
@rest_anonymous()
def signup(request, *args, **kwargs):
    serialized = UserSerializer(data=request.data, context={'request': request})
    if serialized.is_valid():
        user = serialized.save()
        ret = serialized.data
        token = Token.objects.get(user=user)
        try:
            g = Group.objects.get(name='user')
            g.user_set.add(user)
            ret['groups'] = ['user']
        except Exception:
            logger.debug("'user' group isn't exist. ")
        ret['id'] = user.id
        ret['token'] = token.key
        return Response(ret)
    else:
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
