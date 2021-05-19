from django import forms


class UrlForm(forms.Form):
    longUrl = forms.URLField()
