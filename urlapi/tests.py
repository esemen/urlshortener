from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase

from urlapi.models import Urls, UrlStat
from urlapi.views import TemplateListAll, urlRedirect


class UrlModelsTestCase(TestCase):
    def setUp(self):
        urls = Urls.objects.create(longUrl="https://www.datametric.uk", shortUrl="wrlc.shrt/XYvxsd",
                                   shortCode="XYvxsd")
        UrlStat.objects.create(url=urls)

    def test_url_UrlStatCreate(self):
        url = Urls.objects.get(shortCode="XYvxsd")
        urlStat = UrlStat.objects.get(url=url)
        self.assertEqual(url.shortCode, 'XYvxsd')
        self.assertEqual(urlStat.url.longUrl, 'https://www.datametric.uk')

    def test_index_view(self):
        response = self.client.get(reverse('url-list'))
        assert response.status_code == 200


class HomePageTest(TestCase):
    def setUp(self):
        urls = Urls.objects.create(longUrl="https://www.datametric.uk", shortUrl="wrlc.shrt/XYvxsd",
                                   shortCode="XYvxsd")
        UrlStat.objects.create(url=urls)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, TemplateListAll)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        request.method = 'GET'
        response = TemplateListAll(request)
        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        self.assertIn(b'<title>Url Shortner Service</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

    def test_redirectUrl(self):
        request = HttpRequest()
        request.method = 'GET'
        response = urlRedirect(request, "XYvxsd")
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)


# View/Template Test
class UrlCreateAPIViewTestCase(APITestCase):
    def test_CreateUrlApi(self):
        url = reverse('url-list')

        # Not Valid Url Test
        datanovalid = {'longUrl': 'google.cor'}
        response = self.client.post(url, datanovalid, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Valid Test
        data = {'longUrl': 'https://www.datametric.uk'}
        response = self.client.post(url, data, format='json')
        shortCode = response.json()['shortCode']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Object Test
        self.assertEqual(Urls.objects.count(), 1)
        self.assertEqual(Urls.objects.get().longUrl, 'https://www.datametric.uk')
        self.assertEqual(Urls.objects.get().shortCode, shortCode)

        # GetLists
        responseGetList = self.client.get(url, format='json')
        self.assertEqual(responseGetList.status_code, status.HTTP_200_OK)
        self.assertIn(b'shortUrl', response.content)

        # GetUrl
        getUrl = self.client.get("http://localhost:8000/url/" + shortCode)
        self.assertEqual(getUrl.status_code, status.HTTP_200_OK)

        # Delete
        getUrl = self.client.delete("http://localhost:8000/url/" + shortCode)
        self.assertEqual(getUrl.status_code, status.HTTP_204_NO_CONTENT)
