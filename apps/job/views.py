from django.contrib import messages
from hitcount.views import HitCountDetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from job.models import Job

class JobList(ListView):
    model = Job
    template_name = 'job/job_list.html'
    context_object_name = 'job'
    paginate_by = 8
    
    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get('name')
        job = Job.objects.published_job_lists(query)
        if query is not None:
            job_length = len(job)
            messages.success(self.request, f"{job_length if job_length >=1  else 'No'} items found for {query}.")
        return job
job_list = JobList.as_view()

@method_decorator(login_required, name='dispatch')
class JobDetail(HitCountDetailView):
    model = Job
    template_name = "job/job_detail.html"
    context_object_name = "job"
    slug_field = 'slug'
    count_hit = True
job_detail = JobDetail.as_view()
