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
        route='create/',
        view=views.shortener_api_createview,
        name='shortener_create'
    ),
    path(
        route='link/',
        view=views.shortener_api_retrieveview,
        name='shortener_link'
    ),
]
