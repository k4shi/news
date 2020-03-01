from rest_framework.serializers import ModelSerializer

from backend.news.models.news import News


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'content')
