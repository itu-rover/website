from collections import OrderedDict

from django.views.generic import TemplateView
from django.http import Http404

from core.utils import current_year

from .models import SponsorshipType


class SponsorsPage(TemplateView):
    template_name = 'sponsors.html'
    not_found_message = 'Year not found for sponsors page.'

    def get_sponsor_context(self, year):
        result_sponsor_types = OrderedDict()
        sponsor_types = (SponsorshipType.objects
                         .prefetch_related('sponsors').all())
        for sponsor_type in sponsor_types:
            years_sponsors = (sponsor_type.sponsors
                              .filter(sponsorship_year=year))
            if years_sponsors:
                result_sponsor_types[sponsor_type] = years_sponsors
        return {
            'sponsor_types': result_sponsor_types,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        year = self.kwargs.get('year', current_year())
        sponsor_context = self.get_sponsor_context(year)
        if not sponsor_context:
            raise Http404(self.not_found_message)
        context.update(sponsor_context)
        return context


class SupportPage(TemplateView):
    template_name = 'support.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = {
            'sponsorship_types': SponsorshipType.objects.all(),
        }
        context.update(extra_context)
        return context
