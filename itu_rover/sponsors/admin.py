from django.contrib import admin

from core.admin import PagedownedModelAdmin, OrderableModelAdmin
from .models import Sponsor, SponsorshipType, SupportPage


admin.site.register(Sponsor)


@admin.register(SponsorshipType)
class SponsorshipTypeModelAdmin(OrderableModelAdmin, PagedownedModelAdmin):
    pass


@admin.register(SupportPage)
class SupportPageModelAdmin(PagedownedModelAdmin):
    pass
