# apps.shortenurl.models.py

from random import choices
from string import ascii_letters

from django.db import models


class Link(models.Model):

    original_link = models.URLField(
        verbose_name="original link",
        max_length=200
    )
    shortened_link = models.URLField(
        verbose_name="original link",
        max_length=200
    )
    created_date = models.DateField(
        verbose_name="created date",
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_date']
        indexes = [models.Index(fields=['id'])]
        verbose_name_plural = "shorten urls"

    def __str__(self):
        return f"{self.original_link} shorten to {self.shortened_link}"

    def save(self, *args, **kwargs):
        if not self.shortened_link:
            self.generate_shorten_url()
        super().save(*args, **kwargs)

    def generate_shorten_url(self):
        from django.conf import settings
        random_string = ''.join(choices(ascii_letters, k=6))
        self.shortened_link = settings.HOST_URL + '/' + random_string
