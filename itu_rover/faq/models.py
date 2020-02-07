from django.db import models
from core.mixins import OrderableMixin
# Create your models here.


class FaqEntry(OrderableMixin):
    """ Entries on the FAQ page """
    question = models.TextField(
        verbose_name='question',
    )
    answer = models.TextField(
        verbose_name='answer',
    )
    eng_question = models.TextField(
        verbose_name='eng_question',
    )
    eng_answer = models.TextField(
        verbose_name='eng_answer',
    )

    def __str__(self):
        return self.question