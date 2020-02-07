from django.contrib import admin

# Register your models here.
from core.admin import PagedownedModelAdmin, OrderableModelAdmin
from .models import FaqEntry


@admin.register(FaqEntry)
class AboutAdmin(OrderableModelAdmin, PagedownedModelAdmin):
    pass
