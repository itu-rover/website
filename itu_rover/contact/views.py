from django.shortcuts import render
from .models import *

# Create your views here.


def ContactPage(request):
    contact_dict = {}

    if JoinForm.objects.all().exists():
        join_form = JoinForm.objects.get()
        contact_dict['join_form'] = join_form

    return render(request, 'contact.html', contact_dict)

