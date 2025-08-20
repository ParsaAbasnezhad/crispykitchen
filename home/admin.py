from django.contrib import admin
from .models import TeamMember, CategoryNewsletter, Newsletter, CategoryEvent, Event, Account

admin.site.register(Newsletter)
admin.site.register(CategoryNewsletter)
admin.site.register(CategoryEvent)
admin.site.register(Event)
admin.site.register(Account)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'responsibility')
    search_fields = ('name', 'responsibility')
