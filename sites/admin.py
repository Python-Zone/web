from django.contrib import admin
from .models import Site


class SiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'show_url', 'update_time', 'create_time')
    list_filter = ['kind', 'create_time']
    search_fields = ['name', 'url']

    def show_url(self, obj):
        return '<a target="_blank" href="%s">%s</a>' % (obj.url, obj.url)
    show_url.allow_tags = True

admin.site.register(Site, SiteAdmin)
