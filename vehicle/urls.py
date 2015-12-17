
from django.conf.urls import patterns, url, include
from .terminalapis import CollectVehicleData

urlpatterns = [
    url('tapi/$', CollectVehicleData.as_view()),
]
