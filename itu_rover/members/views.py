from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist

from .models import SubTeam, TeamAdvisor, Member, TeamLeader, MembersPage as MP


class MembersPage(TemplateView):
    template_name = 'members.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            leader = TeamLeader.objects.get().member
        except ObjectDoesNotExist:
            leader = None
        extra_context = {
            'subteams': SubTeam.objects.prefetch_related('members').all(),
            'advisors': TeamAdvisor.objects.all(),
            'leader': leader,
            'subteamless': Member.objects.filter(subteam=None),
            'page': MP.objects.get(),
        }
        context.update(extra_context)
        return context
