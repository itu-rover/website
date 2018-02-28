from django.db import models

from core.mixins import OrderableMixin


class RoverEntry(OrderableMixin):
    """ Entries on the rover page """
    title = models.CharField(
        max_length=50,
        verbose_name='title',
    )
    detail = models.TextField(
        verbose_name='detail',
    )
    image = models.ImageField(
        upload_to='images/rover',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title
