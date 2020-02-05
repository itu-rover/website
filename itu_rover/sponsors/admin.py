from django.contrib import admin

from core.admin import PagedownedModelAdmin, OrderableModelAdmin
from .models import sponsor_new, sponsor_type, SupportPage


@admin.register(sponsor_new)
class SponsorAdmin(admin.ModelAdmin):
    list_filter = [
        'sponsorship_year',
        #'sponsorship_type',
    ]


@admin.register(sponsor_type)
class SponsorshipTypeModelAdmin(OrderableModelAdmin, PagedownedModelAdmin):
    pass


@admin.register(SupportPage)
class SupportPageModelAdmin(PagedownedModelAdmin):
    pass
