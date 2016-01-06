from django.shortcuts import render
import calendar
import datetime
from dateutil.relativedelta import relativedelta
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_400_BAD_REQUEST
from models import UserSavingEnergyPerDay, UserSavingEnergyPerMonth
from serializers import UserSavingEnergyPerDaySerilizer, UserSavingEnergyPerMonthSerilizer

# Create your views here.

@api_view(['GET'])
def month_archive(request, year, month):
    year = int(year)
    month = int(month)
    uid = request.user.id
    # print("year:%s, month:%s, user_id:%s" % (year, month, uid))
    (weekday, num_of_days) = calendar.monthrange(year, month)
    firstday = datetime.datetime(year, month, 1)
    lastday = datetime.datetime(year, month, num_of_days)
    queryset = UserSavingEnergyPerDay.objects.filter(timestamp__gte=firstday, timestamp__lte=lastday, uid=uid).order_by('timestamp')
    serializer = UserSavingEnergyPerDaySerilizer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def last_n_month_archive(request, num):
    # print(num)
    num = int(num)
    uid = request.user.id
    now = datetime.datetime.now()
    begin = (now + relativedelta(months=-num)).replace(day=1)
    end = now.replace(day=1)
    queryset = UserSavingEnergyPerMonth.objects.filter(timestamp__gte=begin, timestamp__lt=end, uid=uid).order_by('timestamp')
    serializer = UserSavingEnergyPerMonthSerilizer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def query_energysaving(request, *args, **kwargs):
    if "from" not in request.query_params or "to" not in request.query_params:
        return Response("'from' and 'to' parameter are required.", status=HTTP_400_BAD_REQUEST)
    _from = request.query_params.get("from")
    _to = request.query_params.get("to")
    try:
        _from = datetime.datetime.strptime(_from, '%Y-%m-%d')
        _to = datetime.datetime.strptime(_to, '%Y-%m-%d')
    except ValueError:
        return Response("'from' and 'to' parameter required with '%Y-%m-%d' format", status=HTTP_400_BAD_REQUEST)

    if _from > _to:
        return Response("from must lest than to", status=HTTP_400_BAD_REQUEST)

    uid = request.user.id
    # if in the same month
    if _from.year == _to.year and _from.month == _to.month:
        model_class = UserSavingEnergyPerDay
        serialized_class = UserSavingEnergyPerDaySerilizer
    else:
        model_class = UserSavingEnergyPerMonth
        serialized_class = UserSavingEnergyPerMonthSerilizer
    queryset = model_class.objects.filter(timestamp__gte=_from, timestamp__lte=_to, uid=uid).order_by("timestamp")
    serializer = serialized_class(queryset, many=True)
    return Response(serializer.data)

