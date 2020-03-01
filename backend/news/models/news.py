from django.db import models


class News(models.Model):
    title = models.CharField(max_length=75)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_created=True)

    class Meta:
        app_label = 'news'
        db_table = 'news'
