# backend.shortenurl.serializer.py

from rest_framework.serializers import ModelSerializer
from shortenurl.models import Link


class LinkSerializer(ModelSerializer):

    class Meta:
        model = Link
        fields = ['original_link', 'shortened_link']
