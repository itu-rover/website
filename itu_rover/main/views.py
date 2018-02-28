from django.views.generic.list import ListView

from .models import SliderImage


class MainPage(ListView):
    model = SliderImage
    template_name = 'main.html'
    context_object_name = 'slide_images'
