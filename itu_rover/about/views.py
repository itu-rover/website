from django.views.generic.list import ListView

from .models import AboutEntry


class AboutPage(ListView):
    model = AboutEntry
    template_name = 'about.html'
    context_object_name = 'entries'
