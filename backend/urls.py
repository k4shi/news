from django.conf.urls import url
from django.contrib import admin
from django.urls import include

from backend.news import urls as news_url

api_endpoint_view = [
    url(r'^(?P<version>(v1))/', include(news_url)),
]

urlpatterns = [
    url(r'^api/', include(api_endpoint_view)),
    url('admin/', admin.site.urls),
]
