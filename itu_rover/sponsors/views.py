from collections import OrderedDict

from django.views.generic import TemplateView

from core.utils import current_year

from .models import SponsorshipType


class SponsorsPage(TemplateView):
    template_name = 'sponsors.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        year = self.kwargs.get('year', current_year())
        result_types = OrderedDict()
        types = SponsorshipType.objects.prefetch_related('sponsors').all()
        for type in types:
            years_sponsors = type.sponsors.filter(sponsorship_year=year)
            if years_sponsors:
                result_types[type] = years_sponsors
        extra_context = {
            'types': result_types,
        }
        context.update(extra_context)
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
