from django.views.generic import TemplateView

from core.utils import current_year
from sponsors.views import SponsorsPage
from members.views import MembersPage


class OldYearPage(SponsorsPage, MembersPage):
    template_name = 'old_year.html'
    not_found_message = "Year not found for old year page."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sponsors_page = super(SponsorsPage, self)
        members_page = super(MembersPage, self)
        sponsor_context = sponsors_page.get_context_data()
        member_context = members_page.get_context_data()
        context.update(sponsor_context)
        context.update(member_context)
        return context
