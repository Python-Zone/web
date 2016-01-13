from django.contrib import admin
from .models import Topic, Section, Node


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'show_url', 'update_time', 'create_time')
    list_filter = ['kind', 'publish_time', 'create_time']
    search_fields = ['title', 'url']

    def show_url(self, obj):
        return '<a target="_blank" href="%s">%s</a>' % (obj.url, obj.url)
    show_url.allow_tags = True


class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'weight')


class NodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'section', 'desc', 'weight')


admin.site.register(Topic, TopicAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Node, NodeAdmin)