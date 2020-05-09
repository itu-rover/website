from django.views.generic import TemplateView

from .models import SliderImage, MainPageEntry


class MainPage(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = {
            'slide_images': SliderImage.objects.all(),
            'entries': MainPageEntry.objects.filter(is_old=False),
        }
        context.update(extra_context)
        return context
