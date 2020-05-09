from django.db import models

from core.mixins import OrderableMixin


class AboutEntry(OrderableMixin):
    """ Entries on the about page """
    title = models.CharField(
        max_length=50,
        verbose_name='title',
    )
    detail = models.TextField(
        verbose_name='detail',
    )

    def __str__(self):
        return self.title
