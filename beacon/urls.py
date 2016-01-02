# -*- coding: utf-8 -*-

from django.conf.urls import url
from views import BeaconList, BeaconCheckInCreate

urlpatterns = [
    url('busbeacons/(?P<bid>.+)/$', BeaconList.as_view()),
    url('checkin/$', BeaconCheckInCreate.as_view()),
]
