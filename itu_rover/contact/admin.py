from django.contrib import admin
from .models import *

# Register your models here.


class AdminContact(admin.ModelAdmin):
    list_display = ["name", "text", "email", "date"]
    list_display_links = ["date"]
    list_filter = ["date"]
    search_fields = ["name", "email", "date"]

    class Meta:
        model = ContactForm_model


class AdminSupport(admin.ModelAdmin):
    list_display = ["name"]

    class Meta:
        model = SupportForm


class AdminJoin(admin.ModelAdmin):
    list_display = ["name"]

    class Meta:
        model = JoinForm


admin.site.register(ContactForm_model, AdminContact)
admin.site.register(SupportForm, AdminSupport)
admin.site.register(JoinForm, AdminJoin)


