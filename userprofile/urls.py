
from django.conf.urls import patterns, url, include
import views

urlpatterns = [
    url('curruser/$', views.curruser),
]
