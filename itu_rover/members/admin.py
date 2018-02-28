from django.contrib import admin

from .models import Member, SubTeam, TeamLeader, TeamAdvisor

models = [Member, SubTeam, TeamLeader, TeamAdvisor]
admin.site.register(models)
