# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

# Create your views here.


class FavColorView(APIView):
    FAV_COLOR = 'fav_color'

    def get(self, request):
        if self.FAV_COLOR in request.session:
            msg = '%s in session is %s' % (self.FAV_COLOR, request.session[self.FAV_COLOR])
        else:
            msg = '%s is not found in session' % self.FAV_COLOR
        return Response(msg)

    def post(self, request):
        if self.FAV_COLOR not in request.data:
            return Response("no favourite color set in requeset", status=HTTP_400_BAD_REQUEST)
        else:
            color = request.data.get(self.FAV_COLOR)
            request.session[self.FAV_COLOR] = color
            return Response("favourite color is set to %s" % color)


class ShareColorView(APIView):
    SHARE_COLOR = "share_color"

    def get(self, request):
        color = cache.get(self.SHARE_COLOR)
        if color:
            msg = "%s in cache is %s" % (self.SHARE_COLOR, color)
        else:
            msg = "%s is not found in cache" % self.SHARE_COLOR
        return Response(msg)

    def post(self, request):
        if self.SHARE_COLOR not in request.data:
            return Response("no share_color set in requeset", status=HTTP_400_BAD_REQUEST)
        else:
            color = request.data.get(self.SHARE_COLOR)
            cache.set(self.SHARE_COLOR, color, 30)
            return Response("share color is set to %s" % color)
