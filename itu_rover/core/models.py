from django.db import models


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


class Document(models.Model):
    title = models.CharField(max_length=20)
    document = models.FileField(upload_to='documents')

    def __str__(self):
        return self.title
