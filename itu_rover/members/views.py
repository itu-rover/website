from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.db.models import Prefetch

from core.utils import current_year

from .models import SubTeam, TeamAdvisor, Member, TeamLeader, MembersPage as MP


class MembersPage(TemplateView):
    template_name = 'members.html'
    not_found_message = 'Year not found for members page.'

    def get_members_context(self, year):
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
                    ))
        if not subteams:
            raise Http404(self.not_found_message)
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
        members_context = self.get_members_context(year)
        context.update(members_context)
        return context
