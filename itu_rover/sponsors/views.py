from django.views.generic import TemplateView
from django.http import Http404
from django.db.models import Prefetch

from core.utils import current_year

from .models import SponsorshipType, Sponsor


class SponsorsPage(TemplateView):
    template_name = 'sponsors.html'
    not_found_message = 'Year not found for sponsors page.'

    def get_sponsor_context(self, year):
        years_sponsors = Sponsor.objects.filter(sponsorship_year=year)
        sponsor_types = (SponsorshipType.objects
                         .filter(sponsors__sponsorship_year=year)
                         .prefetch_related(
                             Prefetch('sponsors', queryset=years_sponsors)
                         ))
        if not sponsor_types:
            raise Http404(self.not_found_message)
        return {
            'sponsor_types': sponsor_types,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        year = self.kwargs.get('year', current_year())
        sponsor_context = self.get_sponsor_context(year)
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
