from django.contrib import admin

from .models import Member, SubTeam, TeamLeader, TeamAdvisor, MembersPage

models = [Member, SubTeam, TeamLeader, TeamAdvisor, MembersPage]
admin.site.register(models)
