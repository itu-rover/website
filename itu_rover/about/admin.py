from django.contrib import admin

from adminsortable2.admin import SortableAdminMixin

from core.admin import PagedownedModelAdmin
from .models import AboutEntry


@admin.register(AboutEntry)
class AboutAdmin(SortableAdminMixin, PagedownedModelAdmin):
    pass
