from models import News
from rest_framework import viewsets
from serializers import NewsSerializer


# Create your views here.


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.filter(published=True)
    serializer_class = NewsSerializer
