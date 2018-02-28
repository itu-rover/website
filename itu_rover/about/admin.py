from django.contrib import admin

from core.admin import PagedownedModelAdmin, OrderableModelAdmin
from .models import AboutEntry


@admin.register(AboutEntry)
class AboutAdmin(OrderableModelAdmin, PagedownedModelAdmin):
    pass
