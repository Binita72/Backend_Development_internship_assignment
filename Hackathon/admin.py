from django.contrib import admin
from .models import Hackathonm, Submission

@admin.register(Hackathonm)
class HackathonAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_datetime', 'end_datetime', 'reward_prize')
    search_fields = ('title', 'description', 'reward_prize')

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'hackathon', 'submission_file')
    list_filter = ('hackathon',)
    search_fields = ('name', 'summary')


#admin.site.register(Hackathonm, HackathonAdmin)
#admin.site.register(Submission, SubmissionAdmin)