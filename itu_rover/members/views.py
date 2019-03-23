from collections import OrderedDict

from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from core.utils import current_year

from .models import SubTeam, TeamAdvisor, Member, TeamLeader, MembersPage as MP


class MembersPage(TemplateView):
    template_name = 'members.html'
    not_found_message = 'Year not found for members page.'

    def get_members_context(self, year):
        try:
            leader = TeamLeader.objects.filter(member__year=year).get()
            leader_member = leader.member
        except ObjectDoesNotExist:
            leader_member = None
        result_subteams = OrderedDict()
        subteams = SubTeam.objects.all()
        for subteam in subteams:
            members = subteam.members.filter(year=year)
            if members:
                result_subteams[subteam] = members
        return {
            'subteams': result_subteams,
            'advisors': TeamAdvisor.objects.filter(year=year),
            'leader': leader_member,
            'subteamless': Member.objects.filter(subteam=None, year=year),
            'page': MP.objects.get(),
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        year = self.kwargs.get('year', current_year())
        members_context = self.get_members_context(year)
        if not members_context:
            raise Http404(self.not_found_message)
        context.update(members_context)
        return context
