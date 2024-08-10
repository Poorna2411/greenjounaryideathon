# admin.py

from django.contrib import admin
from .models import Contact
from .models import Submission, TeamMember
from .models import TeamRegistration

admin.site.register(TeamRegistration)


class TeamMemberInline(admin.TabularInline):
    model = TeamMember

class SubmissionAdmin(admin.ModelAdmin):
    inlines = [
        TeamMemberInline,
    ]
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(TeamMember)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date_submitted')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('date_submitted',)
