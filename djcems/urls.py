"""djcems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken import views
from filebrowser.sites import site
from userprofile.views import UserViewSet, GroupViewSet
from beacon.views import BeaconViewSet


# rest_framework routes
router = routers.DefaultRouter()
router.register(r'api/user', UserViewSet)
router.register(r'api/group', GroupViewSet)
router.register(r'api/beacon', BeaconViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/filebrowser/', include(site.urls)),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token),

    url(r'^userprofile/', include('userprofile.urls')),
    url(r'^vehicle/', include('vehicle.urls')),
    url(r'^sms/', include('sms.urls')),
    url(r'^beacon/', include('beacon.urls')),
    url(r'^hello/', include('hello.urls')),

    url(r'^tinymce/', include('tinymce.urls')),
]


from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
