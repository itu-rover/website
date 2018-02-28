from django.contrib import admin

from core.admin import OrderableModelAdmin, PagedownedModelAdmin
from .models import RoverEntry


@admin.register(RoverEntry)
class RoverEntryAdmin(OrderableModelAdmin, PagedownedModelAdmin):
    pass
