
from django.conf.urls import patterns, url, include
from views import FavColorView, ShareColorView

urlpatterns = [
    url('favcolor/$', FavColorView.as_view()),
    url('sharecolor/$', ShareColorView.as_view()),
]
