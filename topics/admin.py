from django.contrib import admin
from .models import Topic


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'show_url', 'site', 'update_time', 'create_time')
    list_filter = ['site', 'publish_time', 'create_time']
    search_fields = ['title', 'url']

    def show_url(self, obj):
        return '<a target="_blank" href="%s">%s</a>' % (obj.url, obj.url)
    show_url.allow_tags = True

admin.site.register(Topic, TopicAdmin)