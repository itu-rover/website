from django.contrib import admin

from .models import Sponsor, SponsorshipType


models = [Sponsor, SponsorshipType]
admin.site.register(models)
