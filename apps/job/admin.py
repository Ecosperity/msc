from django.contrib import admin
from .models import Job, JobApplicant

class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'slug', 'publish')

admin.site.register(Job, JobAdmin)
admin.site.register(JobApplicant)