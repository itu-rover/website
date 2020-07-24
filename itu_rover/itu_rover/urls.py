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
from main.views import MainPage
from rover.views import RoverPage
from sponsors.views import SponsorsPage
from oldyears.views import OldYearPage
from contact.views import ContactPage

urlpatterns = [
    path('manage/', admin.site.urls),
    path('', MainPage.as_view(), name='main'),
    path('hakkında/', AboutPage.as_view(), name='about'),
    path('takım-üyeleri/', MembersPage.as_view(), name='members'),
    path('takım-üyeleri/<int:year>/', MembersPage.as_view(),
         name='members-with-year'),
    path('sponsorlar/', SponsorsPage.as_view(), name='sponsors'),
    path('sponsorlar/<int:year>/', SponsorsPage.as_view(),
         name='sponsors-with-year'),
    path('rover/', RoverPage.as_view(), name='rover'),
    path('geçmiş/<int:year>/', OldYearPage.as_view(), name='oldyear'),
    path('iletişim', ContactPage, name='contact'),

    # English Part -----------------------------------------
    path('eng/', MainPage.as_view(), name='eng_main'),
    path('eng/hakkında/', AboutPage.as_view(), name='eng_about'),
    path('eng/takım-üyeleri/', MembersPage.as_view(), name='eng_members'),
    path('eng/takım-üyeleri/<int:year>/', MembersPage.as_view(),
         name='members-with-year'),
    path('eng/sponsorlar/', SponsorsPage.as_view(), name='eng_sponsors'),
    path('eng/sponsorlar/<int:year>/', SponsorsPage.as_view(),
         name='sponsors-with-year'),
    path('eng/rover/', RoverPage.as_view(), name='eng_rover'),
    path('eng/geçmiş/<int:year>/', OldYearPage.as_view(), name='eng_oldyear'),
    path('eng/iletişim', ContactPage, name='eng_contact'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = ([
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
      + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
      + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
