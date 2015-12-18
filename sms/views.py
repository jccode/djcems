# -*- coding:utf-8 -*-

import re
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from provider import HuYiSms
from djcems.utils import rest_anonymous

# Create your views here.

mobile_pattern = re.compile(r'^(13|15|18)\d{9}$')
huyi_sms = HuYiSms()

@api_view(['POST'])
@rest_anonymous()
def send_sms(request, *args, **kwargs):
    phone = request.data.get("phone", None)
    if phone is None:
        return Response(data="telphone number should be send as a parameter of \"phone\"", status=HTTP_400_BAD_REQUEST)
    elif not mobile_pattern.match(phone):
        return Response(data="phone is invalid", status=HTTP_400_BAD_REQUEST)
    else:
        # TODO: 加入限制,对同个手机号，必须要等90秒才能进行下一个请求.
        ret = huyi_sms.send(phone)
        if ret == 0:
            return Response(data="send message failed", status=HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(ret)



