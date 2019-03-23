from sponsors.views import SponsorsPage
from members.views import MembersPage


class OldYearPage(SponsorsPage, MembersPage):
    template_name = 'oldyears.html'
    not_found_message = "Year not found for old year page."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        year = self.kwargs.get('year')
        sponsors_page = super(SponsorsPage, self)
        members_page = super(MembersPage, self)
        sponsor_context = sponsors_page.get_context_data()
        member_context = members_page.get_context_data()
        context.update(sponsor_context)
        context.update(member_context)
        context.update(year=year)
        return context
