from django.db import models

from core.mixins import OrderableMixin
from .utils import slider_image_upload_to


class SliderImage(OrderableMixin):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to=slider_image_upload_to)
    show_title = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class MainPageEntry(OrderableMixin):
    title = models.CharField(max_length=30)
    content = models.TextField()

    def __str__(self):
        return self.title
