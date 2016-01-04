
from django.conf.urls import url
from views import app_download


urlpatterns = [
    url('download/app/$', app_download),
]
