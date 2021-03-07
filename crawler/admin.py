from django.contrib import admin
from .models import Link
# Register your models here.


admin.site.site_header = "Crawler"
admin.site.site_title = "scraper"
admin.site.index_title = "link collector"


class Crawler(admin.ModelAdmin):

    def change_name_to_default(self, request, queryset):
        queryset.update(name='default')

    change_name_to_default.short_description = 'none to default'

    list_display = ('name', 'address')
    search_fields = ('address',)
    actions = ('change_name_to_default',)
    fields = ('address',)
    list_editable = ('address',)


admin.site.register(Link, Crawler)

