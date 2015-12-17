
from django.conf.urls import patterns, url, include
import views

urlpatterns = [
    url('curruser/$', views.curruser),
    url('userexist/$', views.userexist),
    url('signup/$', views.signup),
]
