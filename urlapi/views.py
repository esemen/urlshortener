import validators
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.response import Response
from urlapi.forms import UrlForm
from urlapi.models import Urls, UrlStat
from urlapi.serializer import UrlSerializerGet, UrlSerializerPost
from urlapi.utils import createShortenedUrl, ResponseMessage


class UrlList(ListAPIView, CreateModelMixin):
    serializer_class = UrlSerializerGet
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = {
        'shortUrl': ['exact'],
        'shortCode': ['exact'],
        'id': ['exact'],
    }
    search_fields = ('id',)
    ordering_fields = '__all__'
    ordering = ['-id']

    def get_queryset(self):
        queryset = Urls.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = UrlSerializerPost(data=request.data)
        if validators.url(serializer.initial_data['longUrl']):
            serializer.initial_data['shortCode'] = createShortenedUrl()
            serializer.initial_data['shortUrl'] = "wrlc.shrt/" + serializer.initial_data['shortCode']
            if serializer.is_valid():
                serializer.save()
                UrlStat.objects.get_or_create(url_id=serializer.data["id"])
                return JsonResponse(ResponseMessage(message='Short url was created.',
                                                    shortUrl=serializer.data["shortUrl"],
                                                    shortCode=serializer.data["shortCode"]).toJSON(),
                                    status=status.HTTP_201_CREATED, safe=False)
        else:
            return JsonResponse(ResponseMessage(message='Enter a valid URL.').toJSON(),
                                status=status.HTTP_400_BAD_REQUEST, safe=False)


class UrlChange(ListAPIView, RetrieveModelMixin, DestroyModelMixin):
    queryset = Urls.objects.all()
    serializer_class = UrlSerializerGet
    lookup_field = 'shortCode'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(Urls, shortCode=kwargs.get('shortCode'))
        UrlStat.objects.filter(url=instance).update(accessCount=F("accessCount") + 1)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)  # status code default 200

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


def index(request):
    context = {}
    form = UrlForm()
    context['form'] = form
    return render(request, "home.html", context)


def urlRedirect(request, shortCode):
    data = Urls.objects.get(shortCode=shortCode)
    UrlStat.objects.filter(url=data).update(accessCount=F("accessCount") + 1)
    return redirect(data.longUrl)
