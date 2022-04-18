from django.contrib import admin
from home.models import Event, Scores, Team

# Register your models here.
admin.site.register(Event)
admin.site.register(Scores)
admin.site.register(Team)