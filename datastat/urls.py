
from django.conf.urls import url
from views import month_archive, last_n_month_archive, query_energysaving

urlpatterns = [
    url('energysaving/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', month_archive),
    url('energysaving/lastnmonth/(?P<num>[0-9]+)/$', last_n_month_archive),
    url('energysaving/query/$', query_energysaving),
]