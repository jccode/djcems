# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, UserProfileSerializer
from rest_framework.decorators import api_view, authentication_classes, renderer_classes
from rest_framework.response import Response

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


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