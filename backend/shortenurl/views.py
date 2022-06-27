# shortenurl.views.py

import json

from django.views import View
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseBadRequest

from rest_framework import generics, views
from shortenurl.models import Link
from shortenurl.serializer import LinkSerializer


class ShortenerListAPIView(generics.ListAPIView):

    queryset = Link.objects.all()
    serializer_class = LinkSerializer


shortener_api_listview = ShortenerListAPIView.as_view()


class ShortenCreateAPIView(generics.CreateAPIView):

    serializer_class = LinkSerializer


shortener_api_createview = ShortenCreateAPIView.as_view()


class ShortenRetrieveLinkAPIView(views.APIView):

    def post(self, request, *args, **kwargs):

        try:
            link = json.loads(request.body)['link']
            long_link = Link.objects.get(
                shortened_link=f"{settings.HOST_URL}/{link}"
            ).original_link
            return JsonResponse({'link': long_link})
        except KeyError:
            return HttpResponseBadRequest()
        except Link.DoesNotExist:
            return HttpResponseBadRequest()
        except:
            HttpResponseBadRequest()

    def get(self, *args, **kwargs):
        return HttpResponseBadRequest()


shortener_api_retrieveview = ShortenRetrieveLinkAPIView.as_view()


class RedirectorView(View):

    def get(self, request, shortener_link, *args, **kwargs):
        shortened_link = settings.HOST_URL + \
            '/' + self.kwargs['shortener_link']
        redirect_link = Link.objects.filter(
            shortened_link=shortener_link).first().original_link
        return redirect(redirect_link)


redirector_view = RedirectorView.as_view()
