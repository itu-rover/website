from django.db import models

from core.mixins import OrderableMixin
from members.utils import validate_one_object


class Entry(OrderableMixin):
    """ Entry abstract model """
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
    )
    eng_title = models.CharField(
        max_length=50,
        verbose_name='eng_title',
        default="eng",
    )
    eng_detail = models.TextField(
        verbose_name='eng_detail',
        default="eng",
    )

    class Meta(OrderableMixin.Meta):
        abstract = True

    def __str__(self):
        return self.title


class RoverEntry(Entry):
    """ Entries on the rover page """
    pass


class RoverSubEntry(Entry):
    """ Subentries on the rover page """
    parent = models.ForeignKey(
        "RoverEntry",
        on_delete=models.CASCADE,
        related_name='subentries',
        verbose_name='parent of subentry',
    )

    def __str__(self):
        return super().__str__() + " < " + str(self.parent)


class RoverPage(models.Model):
    design_review = models.FileField(
        upload_to='documents/rover',
        blank=True,
        verbose_name='design review file'
    )

    def clean(self):
        validate_one_object(self)

    def __str__(self):
        return "Rover Page"

    class Meta:
        verbose_name = "Rover Page"
        verbose_name_plural = verbose_name
