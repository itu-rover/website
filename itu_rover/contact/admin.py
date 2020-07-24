from django.contrib import admin
from .models import *

# Register your models here.

class AdminJoin(admin.ModelAdmin):
    list_display = ["name"]

    class Meta:
        model = JoinForm

admin.site.register(JoinForm, AdminJoin)


