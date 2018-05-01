from django.views.generic import TemplateView

from .models import RoverEntry, RoverPage as RP


class RoverPage(TemplateView):
    template_name = 'rover.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = {
            'entries': RoverEntry.objects.prefetch_related('subentries').all(),
            'page': RP.objects.get(),
        }
        context.update(extra_context)
        return context
