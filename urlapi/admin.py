from django.contrib import admin
from urlapi.models import Urls, UrlStat


@admin.register(Urls)
class UrlsAdmin(admin.ModelAdmin):
    list_display = ('id', 'longUrl', 'shortUrl')
    ordering = ('-id',)
    search_fields = ('longUrl',)
    readonly_fields = ("created",)
    list_per_page = 50
    date_hierarchy = 'created'


@admin.register(UrlStat)
class UrlStatAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'accessCount')
    ordering = ('-id',)
    search_fields = ('urls__longUrl',)
    list_per_page = 50

