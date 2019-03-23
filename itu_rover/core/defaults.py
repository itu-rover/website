from django.utils import timezone


def current_year():
    return timezone.now().year
