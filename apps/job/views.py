from django.contrib import messages
from hitcount.views import HitCountDetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from job.models import Job, JobApplicant
User = get_user_model()

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user=self.request.user
        context['check_applied_condition'] = 1 in [job.is_applied for job in Job.objects.get(slug=self.kwargs.get('slug')).jobapplicant_set.all().filter(user=user)]
        return context
job_detail = JobDetail.as_view()

@login_required
def apply_job(request, slug):
    job = get_object_or_404(Job, slug=slug)
    user=request.user
    check_applied_condition = 1 in [job.is_applied for job in job.jobapplicant_set.all().filter(user=user)]
    if check_applied_condition:
        return redirect("job:job_detail", slug=job.slug)
    try:
        applicant = JobApplicant.objects.get(user=user)
    except:
        applicant=None
    if request.method=="POST":

        notice_period=request.POST.get('notice_period')
        resume=request.FILES['resume']
        name=request.POST['name']
        mobile=request.POST['mobile'
        ]
        user.name=name
        user.mobile=mobile
        user.save()
        try:
            applicant = JobApplicant.objects.get(user=user)
            applicant.notice_period=notice_period
            applicant.resume=resume
        except:
            applicant = JobApplicant(
                        user=user,
                        notice_period=notice_period,
                        is_applied=1,
                        resume=resume,
                    )
        applicant.save()
        applicant.job.add(job)
        job.job_applied_count=job.job_applied_count + 1 if job.job_applied_count else 1
        job.save()
        applicant.save()

        messages.success(request, "you have succesfully applied for the job")
        return redirect("job:job_detail", slug=job.slug)
    context = {
        'check_applied_condition':check_applied_condition,
        'applicant':applicant
    }
    return render(request, 'job/apply_job.html', context)