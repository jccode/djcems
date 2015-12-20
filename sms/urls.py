# -*- coding:utf-8 -*-

from django.conf.urls import url
from views import send_sms

urlpatterns = [
    url('send/$', send_sms)
]