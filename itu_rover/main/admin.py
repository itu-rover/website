from django.contrib import admin

from core.admin import OrderableModelAdmin, PagedownedModelAdmin
from .models import SliderImage, MainPageEntry, MainRovers


@admin.register(SliderImage)
class SliderImageAdmin(OrderableModelAdmin):
    pass


@admin.register(MainPageEntry)
class MainPageEntryAdmin(OrderableModelAdmin, PagedownedModelAdmin):
    pass

@admin.register(MainRovers)
class MainRoversAdmin(OrderableModelAdmin, PagedownedModelAdmin):
    pass
