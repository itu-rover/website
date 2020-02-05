from django.views.generic.list import ListView

#from members.models import MembersPage

from .models import AboutEntry


class AboutPage(ListView):
    model = AboutEntry
    template_name = 'about.html'
    context_object_name = 'entries'
"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proposal'] = MembersPage.objects.get().proposal
        return context
"""