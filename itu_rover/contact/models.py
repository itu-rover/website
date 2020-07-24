from django.db import models

# Create your models here.


class JoinForm(models.Model):
    name = models.CharField(max_length=20)
    form_link = models.TextField(verbose_name="Link of the join form:")
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name