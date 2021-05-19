from django.db import models


class Urls(models.Model):
    longUrl = models.CharField(max_length=255)
    shortUrl = models.CharField(max_length=255, unique=True, blank=True)
    shortCode = models.CharField(max_length=16, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Create Date", blank=True)

    class Meta:
        verbose_name = 'Url'
        verbose_name_plural = 'Urls'


class UrlStat(models.Model):
    url = models.ForeignKey(Urls, editable=True, null=False, on_delete=models.CASCADE, related_name='url_track')
    accessCount = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Url Log'
        verbose_name_plural = 'Url Logs'
