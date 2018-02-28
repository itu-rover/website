from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User, Group

from adminsortable2.admin import SortableAdminMixin
from pagedown.widgets import AdminPagedownWidget

from .models import Document


admin.site.unregister([User, Group])
admin.site.register(Document)


class PagedownedModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }


class OrderableModelAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
