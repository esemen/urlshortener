import json
import string

from django.conf import settings
from random import choice
from string import ascii_letters, digits

from django.utils.crypto import get_random_string

from urlShortener.settings import MAX_CHAR_URLSHORTENER
from urlapi.models import Urls


def createShortenedUrl():
    randomUrlCode = get_random_string(MAX_CHAR_URLSHORTENER, allowed_chars=string.ascii_letters + string.digits)
    while Urls.objects.filter(shortCode=randomUrlCode).exists():
        randomUrlCode = get_random_string(MAX_CHAR_URLSHORTENER, allowed_chars=string.ascii_letters + string.digits)
    return randomUrlCode


class ResponseMessage:
    def __init__(self, **kwargs):
        self.message = kwargs.get('message', '')
        self.shortUrl = kwargs.get("shortUrl", '')
        self.shortCode = kwargs.get("shortCode", '')
        self.errors = kwargs.get("errors", "")

    def toJSON(self):
        return self.__dict__
