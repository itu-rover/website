from django.views.generic import TemplateView

from .models import SubTeam, TeamAdvisor, Member, TeamLeader


class MembersPage(TemplateView):
    template_name = 'members.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = {
            'subteams': SubTeam.objects.prefetch_related('members').all(),
            'advisors': TeamAdvisor.objects.all(),
            'leader': TeamLeader.objects.get(),
            'subteamless': Member.objects.filter(subteam=None),
        }
        context.update(extra_context)
        return context
