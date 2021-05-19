from django.contrib import admin
from django.urls import path
from rest_framework.documentation import include_docs_urls

from urlapi.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path("<slug:shortCode>", urlRedirect, name="redirect"),
    path('url/', UrlList.as_view(), name='url-list'),
    path('url/<slug:shortCode>', UrlChange.as_view(), name='get-url'),

    path('apidoc/', include_docs_urls(title='Url Shortener API', description="All api details here")),
]
