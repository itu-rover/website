from django.contrib import admin
from django import forms

from .models import Member, SubTeam, TeamLeader, TeamAdvisor, MembersPage

models = [TeamLeader, TeamAdvisor, MembersPage]
admin.site.register(models)


class SubTeamAdminForm(forms.ModelForm):
    class Meta:
        model = SubTeam
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #subteam_name = self.initial['name']
        #self.fields['leaders'].queryset = (Member.objects
        #                                   .filter(subteam__name=subteam_name))


@admin.register(SubTeam)
class SubTeamAdmin(admin.ModelAdmin):
    form = SubTeamAdminForm
    filter_horizontal = ['leaders']


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_filter = ['year', 'subteam']
