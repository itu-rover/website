from django.views.generic.list import ListView
from django.conf.urls import include, url
from django.urls import path
from django.shortcuts import render


#from members.models import MembersPage

from .models import FaqEntry


class FaqPage(ListView):
    model = FaqEntry
    template_name = 'faq.html'
    context_object_name = 'faq'





    """def eng_request(request):
        url_faq = '/eng/faq/'
        return render(request, 'faq.html', {"url": url})"""


"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proposal'] = MembersPage.objects.get().proposal
        return context
"""