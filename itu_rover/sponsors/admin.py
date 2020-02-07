from django.contrib import admin

from core.admin import PagedownedModelAdmin, OrderableModelAdmin
from .models import Sponsor, SponsorshipType, SupportPage


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_filter = [
        'sponsorship_year',
        'sponsorship_type',
    ]


@admin.register(SponsorshipType)
class SponsorshipTypeModelAdmin(OrderableModelAdmin, PagedownedModelAdmin):
    pass


@admin.register(SupportPage)
class SupportPageModelAdmin(PagedownedModelAdmin):
    pass
