from django.shortcuts import render
from .models import *
from .forms import ContactForm

# Create your views here.

def ContactPage(request):
    contact_form = ContactForm()
    contact_dict = {
        "contact_form": contact_form,
    }
    if SupportForm.objects.all().exists():
        support_form = SupportForm.objects.get()
        contact_dict['support_form'] = support_form

    if JoinForm.objects.all().exists():
        join_form = JoinForm.objects.get()
        contact_dict['join_form'] = join_form

    return render(request, 'contact.html', contact_dict)


def ContactPage1(request):
    form = ContactForm(request.GET)
    if form.is_valid:
        form.save()
    return render(request, 'form_done.html', {})
