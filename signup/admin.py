from django.contrib import admin

from signup.models import *

class TourneyAdmin(admin.ModelAdmin):
	list_display = ('name', 'active', 'has_alternate_list')


admin.site.register(Tourney, TourneyAdmin)
admin.site.register(Entrant)

