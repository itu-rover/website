"""itu_rover URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

from about.views import AboutPage
from members.views import MembersPage
from faq.views import FaqPage
from main.views import MainPage, GraduatedPage
from rover.views import RoverPage
from sponsors.views import SponsorsPage
from oldyears.views import OldYearPage

urlpatterns = [
    path('manage/', admin.site.urls),
    path('', MainPage.as_view(), name='main'),
    path('eng/', MainPage.as_view(), name='main'),
    path('gecmis/<int:year>/', OldYearPage.as_view(), name='gecmis'),
    path('eng/past/<int:year>/', OldYearPage.as_view(), name='oldyear'),
    path('mezunlar/', GraduatedPage.as_view(), name='mezunlar'),
    path('eng/graduated/', GraduatedPage.as_view(), name='graduated'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = ([
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
      + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
      + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
