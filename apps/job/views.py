from django.views.generic import ListView
from job.models import Job

class HomeView(ListView):
    model = Job
    template_name = 'index.html'