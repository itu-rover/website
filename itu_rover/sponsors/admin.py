from django.contrib import admin

from core.admin import PagedownedModelAdmin, OrderableModelAdmin
from .models import Sponsor, SponsorshipType


admin.site.register(Sponsor)


@admin.register(SponsorshipType)
class SponsorshipTypeModelAdmin(OrderableModelAdmin, PagedownedModelAdmin):
    pass
