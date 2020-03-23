from django.views.generic import TemplateView

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Prefetch

from sponsors.views import SponsorsPage
from members.views import MembersPage

from faq.models import FaqEntry
from about.models import AboutEntry
from sponsors.models import SponsorshipType, Sponsor
from members.models import SubTeam, TeamAdvisor, Member, TeamLeader, MembersPage as MP
from rover.models import RoverEntry, RoverPage as RP
from .models import OldYear


class OldYearPage(TemplateView):
    template_name = 'oldyears.html'
    not_found_message = 'Year not found for old year page.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        year = int(self.kwargs.get('year'))
        print(year)
        oldyear = OldYear.objects.filter(year=year).get()
        sponsor_context = SponsorsPage.get_sponsor_context(self, year)
        member_context = MembersPage.get_member_context(self, year)
        context.update(oldyear=oldyear, **sponsor_context, **member_context)
        return context
