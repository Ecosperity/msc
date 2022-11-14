from django.views.generic import ListView
from .models import Job

class HomeView(ListView):
    model = Job
    template_name = 'index.html'