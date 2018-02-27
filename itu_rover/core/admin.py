from django.contrib import admin
from django.db import models

from pagedown.widgets import AdminPagedownWidget

from .models import SliderImage

admin.site.register(SliderImage)


class PagedownedModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
