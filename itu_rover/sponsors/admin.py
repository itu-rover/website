from django.contrib import admin

from adminsortable2.admin import SortableAdminMixin

from core.admin import PagedownedModelAdmin
from .models import Sponsor, SponsorshipType


admin.site.register(Sponsor)


@admin.register(SponsorshipType)
class SponsorshipTypeModelAdmin(SortableAdminMixin, PagedownedModelAdmin):
    pass
