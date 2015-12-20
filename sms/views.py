# -*- coding:utf-8 -*-

import re
from django.core.cache import cache
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from provider import HuYiSms

SMS_KEY = "app:sms:mobile_sms:"
SMS_EXPIRED_TIME = 90
mobile_pattern = re.compile(r'^(13|15|18)\d{9}$')
huyi_sms = HuYiSms()


# create your views here

@api_view(['POST'])
@authentication_classes(())
@permission_classes(())
def send_sms(request):
    phone = request.data.get("phone", None)
    valid, error = phone_valid(phone)
    if not valid:
        return Response(data=error, status=HTTP_400_BAD_REQUEST)
    ret = huyi_sms.send(phone)
    cache.set(SMS_KEY+phone, SMS_EXPIRED_TIME)
    if ret == 0:
        return Response(data="send message failed", status=HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(ret)


def phone_valid(phone):
    if phone is None:
        return False, "telphone number should be send as a parameter of \"phone\""
    if not mobile_pattern.match(phone):
        return False, "phone is invalid"
    # wait 90 seconds to retrieve a new sms code
    if cache.get(SMS_KEY+phone):
        return False, "You should wait util %d seconds to renew a new sms code" % SMS_EXPIRED_TIME
    return True, ""
