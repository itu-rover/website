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
    image = models.ImageField(
        upload_to='images/about',
        blank=True,
    )
    eng_title = models.CharField(
        max_length=50,
        verbose_name='eng_title',
    )
    eng_detail = models.TextField(
        verbose_name='eng_detail',
    )

    def __str__(self):
        return self.title
