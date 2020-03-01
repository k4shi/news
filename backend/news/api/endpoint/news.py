from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from backend.common.rest.viewset import BaseViewSet
from backend.news.api.serializer import NewsSerializer
from backend.news.models.news import News
from backend.news.services.pushes import msg_pushes


class NewsViewSet(BaseViewSet, ListModelMixin, CreateModelMixin):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        msg_pushes(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)