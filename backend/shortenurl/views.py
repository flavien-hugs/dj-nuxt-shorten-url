# shortenurl.views.py

from django.views import View
from django.conf import settings
from django.shortcuts import render, redirect

from shortenurl.models import Link
from shortenurl.serializer import LinkSerializer
from rest_framework.generics import ListAPIView, CreateAPIView


class ShortenerListAPIView(ListAPIView):

    queryset = Link.objects.all()
    serializer_class = LinkSerializer


shortener_api_listview = ShortenerListAPIView.as_view()


class ShortenCreateAPIView(CreateAPIView):

    serializer_class = LinkSerializer


shortener_api_createview = ShortenCreateAPIView.as_view()


class RedirectorView(View):

    def get(self, request, shortener_link, *args, **kwargs):
        shortened_link = settings.HOST_URL + \
            '/' + self.kwargs['shortener_link']
        redirect_link = Link.objects.filter(
            shortened_link=shortener_link).first().original_link
        return redirect(redirect_link)


redirector_view = RedirectorView.as_view()
