from django.views.generic import TemplateView

from sponsors.views import SponsorsPage
from members.views import MembersPage

from .models import OldYear


class OldYearPage(TemplateView):
    template_name = 'oldyears.html'
    not_found_message = 'Year not found for old year page.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        year = self.kwargs.get('year')
        oldyear = OldYear.objects.filter(year=year).get()
        sponsor_context = SponsorsPage.get_sponsor_context(self, year)
        member_context = MembersPage.get_member_context(self, year)
        context.update(oldyear=oldyear, **sponsor_context, **member_context)
        return context
