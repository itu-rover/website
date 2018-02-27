from django.db import models

from .utils import slider_image_upload_to


class TimeStampedModel(models.Model):
    """
    An abstract base class that provides self-updating
    'created' and 'modified' fields.
    """
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True


class SliderImage(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to=slider_image_upload_to)
    show_title = models.BooleanField(default=False)
    priority = models.PositiveSmallIntegerField(default=10)

    class Meta:
        ordering = ('priority', 'title', )

    def __str__(self):
        return self.title


class Document(models.Model):
    title = models.CharField(max_length=20)
    document = models.FileField(upload_to='documents')

    def __str__(self):
        return self.title
