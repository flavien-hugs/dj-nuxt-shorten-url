# backend.urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from shortenurl.views import redirector_view

redirect_to_api = RedirectView.as_view(url='api/')


urlpatterns = [
    path(route='', view=redirect_to_api),
    path('api/', include('shortenurl.urls')),
    path(
        route='<str:shortener_link>/',
        view=redirector_view,
        name='redirector'
    ),

    path('admin/', admin.site.urls),
]
