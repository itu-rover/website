from django.contrib import admin

from core.admin import PagedownedModelAdmin, OrderableModelAdmin
from .models import FaqEntry


@admin.register(FaqEntry)
class AboutAdmin(OrderableModelAdmin, PagedownedModelAdmin):
    pass
