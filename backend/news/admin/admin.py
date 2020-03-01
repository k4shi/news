from django.contrib import admin

from backend.news.models.news import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


admin.site.register(News, NewsAdmin)
