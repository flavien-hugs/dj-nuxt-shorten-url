# shortenurl.urls.py

from django.urls import path

from shortenurl import views


urlpatterns = [
    path(
        route='',
        view=views.shortener_api_listview,
        name='shortener_list'
    ),
    path(
        route='edit/',
        view=views.shortener_api_createview,
        name='shortener_create'
    ),
]
