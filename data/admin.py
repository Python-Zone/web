from django.contrib import admin
from .models import Community


class CommunityAdmin(admin.ModelAdmin):
    list_display = ('id', 'community_name', 'show_url', 'update_time', 'create_time')
    list_filter = ['update_time', 'create_time']
    search_fields = ['community_name', 'url']

    def show_url(self, obj):
        return '<a target="_blank" href="%s">%s</a>' % (obj.url, obj.url)
    show_url.allow_tags = True


admin.site.register(Community, CommunityAdmin)
