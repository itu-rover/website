from django.views.generic import TemplateView
from django.db.models import Prefetch
from django.http import Http404

from .models import SliderImage, MainPageEntry
from sponsors.models import SponsorshipType, Sponsor

from core.defaults import current_year


class MainPage(TemplateView):
    template_name = 'main.html'
    not_found_message = 'Year not found for sponsors in main page.'

    def get_sponsor_context(self, year):
        # defining year
        if not Sponsor.objects.filter(sponsorship_year=year).exists():
            year = int(year) - 1

        years_sponsors = Sponsor.objects.filter(sponsorship_year=year)
        sponsor_types = (SponsorshipType.objects
                         .filter(sponsors__sponsorship_year=year)
                         .prefetch_related(
                             Prefetch('sponsors', queryset=years_sponsors)
                         )).distinct()
        #if not sponsor_types:
            #raise Http404(self.not_found_message)
        return {
            'sponsor_types': sponsor_types,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        year = self.kwargs.get('year', current_year())
        sponsor_context = self.get_sponsor_context(year)
        extra_context = {
            'slide_images': SliderImage.objects.all().order_by('-title'),
            'entries': MainPageEntry.objects.filter(is_old=False),
        }
        context.update(extra_context)
        context.update(sponsor_context)
        return context
