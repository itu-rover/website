from django.db import models

from core.mixins import OrderableMixin
from core.models import TimeStampedModel
from .utils import slider_image_upload_to


class SliderImage(OrderableMixin, TimeStampedModel):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to=slider_image_upload_to)
    show_title = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class MainPageEntry(OrderableMixin, TimeStampedModel):
    title = models.CharField(max_length=30)
    content = models.TextField()
    is_old = models.BooleanField(
        default=False,
        help_text='is this entry still newsworthy??'
    )

    def __str__(self):
        return self.title
