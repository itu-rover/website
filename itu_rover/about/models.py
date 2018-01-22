from django.db import models


class AboutEntry(models.Model):
    """ Entries on the about page """
    title = models.CharField(
        max_length=50,
        verbose_name='title',
    )
    detail = models.TextField(
        verbose_name='detail',
    )
