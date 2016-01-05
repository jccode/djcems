# -*- coding: utf-8 -*-

from django.conf.urls import url
from views import BeaconList, BeaconCheckin

urlpatterns = [
    url('busbeacons/(?P<bid>.+)/$', BeaconList.as_view()),
    url('checkin/$', BeaconCheckin.as_view()),
]
