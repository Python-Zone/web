from django.contrib import admin
from .models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'company', 'show_url', 'update_time', 'create_time')
    list_filter = ['city', 'publish_time', 'create_time']
    search_fields = ['title', 'company', 'url']

    def show_url(self, obj):
        return '<a target="_blank" href="%s">%s</a>' % (obj.url, obj.url)
    show_url.allow_tags = True

admin.site.register(Job, JobAdmin)