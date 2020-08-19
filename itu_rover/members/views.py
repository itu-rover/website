from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.db.models import Prefetch

from core.defaults import current_year

from .models import SubTeam, TeamAdvisor, Member, TeamLeader, MembersPage as MP
from oldyears.models import OldYear


# MemebersPage class. Members sayfasına istek geldiğinde çalışır. 
# 'year' parametresini doğru tanımlamak önemlidir.
# Sistemi tıpkı Sponsorlar sayfasında olduğu gibidir.
class MembersPage(TemplateView):
    template_name = 'members.html'
    not_found_message = 'Year not found for members page.'

    def get_member_context(self, year):
        # defining year
        if not Member.objects.filter(year=year).exists():
            year = int(year) - 1

        try:
            leader = TeamLeader.objects.filter(member__year=year).get().member
        except ObjectDoesNotExist:
            leader = None
        try:
            members_page = MP.objects.filter(year=year).get()
        except ObjectDoesNotExist:
            members_page = None
        years_members = Member.objects.filter(year=year)
        subteams = (SubTeam.objects
                    .filter(members__year=year)
                    .prefetch_related(
                        Prefetch('members', queryset=years_members)
                    )).distinct()
        return {
            'subteams': subteams,
            'advisors': TeamAdvisor.objects.filter(year=year),
            'leader': leader,
            'subteamless': Member.objects.filter(subteam=None, year=year),
            'page': members_page,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        year = self.kwargs.get('year', current_year())
        member_context = self.get_member_context(year)
        context.update(member_context)
        return context
