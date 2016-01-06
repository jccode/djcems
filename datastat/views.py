from django.shortcuts import render
import calendar
import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_400_BAD_REQUEST
from models import UserSavingEnergyPerDay, UserSavingEnergyPerMonth
from serializers import UserSavingEnergyPerDaySerilizer, UserSavingEnergyPerMonthSerilizer

# Create your views here.

@api_view(['GET'])
def month_archive(request, year, month):
    # print(year + " " + month)
    (weekday, num_of_days) = calendar.monthrange(year, month)
    firstday = datetime.datetime(year, month, 1)
    lastday = datetime.datetime(year, month, num_of_days)
    queryset = UserSavingEnergyPerDay.objects.filter(timestamp__gte=firstday, timestamp__lte=lastday).order_by('timestamp')
    serializer = UserSavingEnergyPerDaySerilizer(queryset, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def last_n_month_archive(request, num):
    # print(num)

    return Response("num: %s" % num)


@api_view(['GET'])
def query_energysaving(request, *args, **kwargs):
    if "from" not in request.query_params or "to" not in request.query_params:
        return Response("'from' and 'to' parameter are required.", status=HTTP_400_BAD_REQUEST)
    _from = request.query_params.get("from")
    _to = request.query_params.get("to")
    return Response("from:"+_from+"; to:"+_to)

