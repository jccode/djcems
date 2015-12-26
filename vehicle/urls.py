
from django.conf.urls import patterns, url, include
from .terminalapis import CollectVehicleData
from views import busData

urlpatterns = [
    url('tapi/$', CollectVehicleData.as_view()),
    url('busdata/(?P<bid>\w+)/$', busData),
]
