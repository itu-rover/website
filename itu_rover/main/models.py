from django.db import models

from core.mixins import OrderableMixin
from core.models import TimeStampedModel
from .utils import slider_image_upload_to


# ---------------------------SLIDER DIDN'T USE-------------------------

class SliderImage(OrderableMixin, TimeStampedModel):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to=slider_image_upload_to)
    show_title = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# ---------------------------MAIN PAGE ENTRIES--------------------------------

class MainPageEntry(OrderableMixin, TimeStampedModel):
    title = models.CharField(max_length=30)
    content = models.TextField()
    is_old = models.BooleanField(
        default=False,
        help_text='is this entry still newsworthy??'
    )
    eng_title = models.CharField(max_length=30)
    eng_content = models.TextField()

    def __str__(self):
        return self.title

# -----------------------ROVERS AT MAINPAGE------------------------------

class MainRovers(OrderableMixin, TimeStampedModel):
    year = models.CharField(max_length=30)
    image = models.ImageField(upload_to=slider_image_upload_to)
    exp = models.TextField()
    exp_eng = models.TextField()

    def __str__(self):
        return self.year
