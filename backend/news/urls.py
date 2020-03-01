from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from backend.news.api.endpoint import NewsViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
