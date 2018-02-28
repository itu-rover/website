from django.contrib import admin
from django.db import models

from adminsortable2.admin import SortableAdminMixin
from pagedown.widgets import AdminPagedownWidget

from .models import SliderImage

admin.site.register(SliderImage)


class PagedownedModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }


class OrderableModelAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
