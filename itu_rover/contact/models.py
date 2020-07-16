from django.db import models

# Create your models here.


class ContactForm_model(models.Model):
    name = models.CharField(
        max_length=120,
        verbose_name="İsminiz, Soyisminiz:"
    )
    text = models.TextField(
        verbose_name="Mesajınız:"
    )
    email = models.EmailField(
        verbose_name="e-Mail adresiniz:"
    )
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class SupportForm(models.Model):
    name = models.CharField(max_length=20)
    form_link = models.TextField(verbose_name="Link of the support form:")
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class JoinForm(models.Model):
    name = models.CharField(max_length=20)
    form_link = models.TextField(verbose_name="Link of the join form:")
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name