from django.contrib import admin

from core.admin import OrderableModelAdmin, PagedownedModelAdmin
from .models import RoverEntry, RoverSubEntry, RoverPage


admin.site.register(RoverPage)


@admin.register(RoverEntry)
class RoverEntryAdmin(OrderableModelAdmin, PagedownedModelAdmin):
    pass


@admin.register(RoverSubEntry)
class RoverSubentryAdmin(OrderableModelAdmin, PagedownedModelAdmin):
    pass
