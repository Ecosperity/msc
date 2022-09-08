from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'slug', 'publish')

admin.site.register(Job, JobAdmin)
