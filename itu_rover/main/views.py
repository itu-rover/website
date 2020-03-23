from django.views.generic import TemplateView

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Prefetch

from .models import SliderImage, MainPageEntry
from faq.models import FaqEntry
from about.models import AboutEntry
from sponsors.models import SponsorshipType, Sponsor
from members.models import SubTeam, TeamAdvisor, Member, TeamLeader, MembersPage as MP
from rover.models import RoverEntry, RoverPage as RP
from oldyears.models import OldYear



class MainPage(TemplateView):
    template_name = 'main.html'
    not_found_message = 'Year not found for sponsors page.'



    def get_sponsor_context(self):
        r_year = str(OldYear.objects.all().order_by('-year')[0].year)
        years_sponsors = Sponsor.objects.filter(sponsorship_year=r_year)
        sponsor_types = (SponsorshipType.objects
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
        years_members = Member.objects.filter(year=r_year)
        subteams = (SubTeam.objects.all().prefetch_related(
            Prefetch('members', queryset=years_members)
        )).distinct()
        return {
            'subteams': subteams,
            'advisors': TeamAdvisor.objects.filter(year=r_year),
            'leader': leader,
            'subteamless': Member.objects.filter(subteam=None, year=year),
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        r_year = str(OldYear.objects.all().order_by('-year')[0].year)

        sponsor_context = self.get_sponsor_context()
        context.update(sponsor_context)
        extra_context = {
            'slide_images': SliderImage.objects.all(),
            'm_entries': MainPageEntry.objects.filter(is_old=False),
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
        years = OldYear.objects.all()
        extra_context = {
            'graduated_members': g_members,
            'years': years,
        }

        context.update(extra_context)

        return context

"""class MainPage(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = {
            'slide_images': SliderImage.objects.all(),
            'entries': MainPageEntry.objects.filter(is_old=False),
        }
        context.update(extra_context)
        return context"""
