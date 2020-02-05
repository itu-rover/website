from django.views.generic import TemplateView

from .models import SliderImage, MainPageEntry, MainRovers
from faq.models import FaqEntry
from about.models import AboutEntry
from sponsors.models import sponsor_new, sponsor_type
from members.models import SubTeam, TeamAdvisor, Member, TeamLeader, MembersPage as MP
from rover.models import RoverEntry, RoverPage as RP
from oldyears.models import OldYear

from core.defaults import current_year
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Prefetch
from django.http import Http404


class MainPage(TemplateView):
    template_name = 'main.html'
    not_found_message = 'Year not found for sponsors page.'



    def get_sponsor_context(self):
        r_year = str(OldYear.objects.all().order_by('-year')[0].year)
        years_sponsors = sponsor_new.objects.filter(sponsorship_year=r_year)
        sponsor_types = (sponsor_type.objects
                         .prefetch_related(
                             Prefetch('sponsors', queryset=years_sponsors)
                         )).distinct()
        return {
            'sponsor_types': sponsor_types,
        }

    def get_member_context(self, year):
        r_year = str(OldYear.objects.all().order_by('-year')[0].year)
        if len(Member.objects.filter(year=r_year)) > 0:
            r_year = str(OldYear.objects.all().order_by('-year')[0].year)
        else:
            r_year = str(OldYear.objects.all().order_by('-year')[1].year)

        try:
            leader = TeamLeader.objects.filter(member__year=r_year).get().member
        except ObjectDoesNotExist:
            leader = None
        print(r_year)
        years_members = Member.objects.filter(year=r_year)
        subteams = (SubTeam.objects.all().prefetch_related(     # filter(members__year=year)
            Prefetch('members', queryset=years_members)
        )).distinct()
        return {
            'subteams': subteams,
            'advisors': TeamAdvisor.objects.filter(year=r_year),
            'leader': leader,
            'subteamless': Member.objects.filter(subteam=None, year=year),
            #'page': members_page,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        r_year = str(OldYear.objects.all().order_by('-year')[0].year)

        sponsor_context = self.get_sponsor_context()
        context.update(sponsor_context)
        extra_context = {
            'slide_images': SliderImage.objects.all(),
            'm_entries': MainPageEntry.objects.filter(is_old=False),
            'rovers': MainRovers.objects.all(),
            'faqs': FaqEntry.objects.all(),
            'about_entries': AboutEntry.objects.all(),
            'r_entries': RoverEntry.objects.prefetch_related('subentries').all(),
        }
        context.update(extra_context)

        member_context = self.get_member_context(r_year)
        context.update(member_context)

        return context

class GraduatedPage(TemplateView):
    template_name = 'graduated.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        g_members = Member.objects.filter(did_work=True)
        extra_context = {
            'graduated_members': g_members
        }

        context.update(extra_context)

        return context