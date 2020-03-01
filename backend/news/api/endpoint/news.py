from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import AllowAny

from backend.common.rest.viewset import BaseViewSet
from backend.news.api.serializer import NewsSerializer
from backend.news.models.news import News


class NewsViewSet(BaseViewSet, ListModelMixin, CreateModelMixin):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (AllowAny,)
