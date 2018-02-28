from django.views.generic import TemplateView

from .models import SponsorshipType, Sponsor


class SponsorsPage(TemplateView):
    template_name = 'sponsors.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = {
            'types': (SponsorshipType.objects
                      .prefetch_related('sponsors')
                      .filter(sponsors__is_old=False).distinct()),
            'old_sponsors': Sponsor.objects.filter(is_old=True),
        }
        context.update(extra_context)
        return context
