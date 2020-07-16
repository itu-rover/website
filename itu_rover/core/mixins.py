from django.db import models


class OrderableMixin(models.Model):
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ('order', )
