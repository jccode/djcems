
from django.conf.urls import url
import views

urlpatterns = [
    url('curruser/$', views.curruser),
    url('userexist/$', views.userexist),
    url('signup/$', views.signup),
]
