from rest_framework import serializers

from urlapi.models import Urls, UrlStat


class UrlSerializerGet(serializers.ModelSerializer):
    count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Urls
        fields = ('shortUrl', 'longUrl', 'shortCode', 'count')

    def get_count(self, obj):
        count = UrlStat.objects.get(url=obj).accessCount
        return count


class UrlSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Urls
        fields = '__all__'


class UrlStatSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = UrlStat
        fields = ('accessCount',)
