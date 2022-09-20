from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.views.generic import ListView, DeleteView
from django.utils.decorators import method_decorator
from django.utils import timezone
import xlwt
from django.urls import reverse_lazy
from apps.dashboard.forms import AddSkillset
from dashboard.models import SkillSet
from apps.functions import allow_access_to
from job.models import Job, JobApplicant, Skill
from job.forms import CreateJobForm

User = get_user_model()

@allow_access_to([User.ADMIN, User.MANAGER])
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

@allow_access_to([User.ADMIN, User.MANAGER])
def create_job(request):
    if request.method == "POST":
        form = CreateJobForm(request.POST)
        skills = request.POST.getlist("skills")
        if form.is_valid():
            publish = form.cleaned_data.get('publish')
            salary = form.cleaned_data.get('salary')
            experience = form.cleaned_data.get('experience')
            if not salary:
                minimum_salary = request.POST.get('minimum_salary')
                maximum_salary = request.POST.get('maximum_salary')
                salary_measurement = request.POST.get('salary_measurement')
                salary_currency = request.POST.get('salary_currency')
                duration = request.POST.get('duration')
                salary = f'{minimum_salary} to {maximum_salary} {salary_measurement} {salary_currency} {duration}'
            if not experience:
                minimum_experience_years = request.POST.get('minimum_experience_years')
                maximum_experience_years = request.POST.get('maximum_experience_years')
                experience = f'{minimum_experience_years} to {maximum_experience_years} Years'
            user=request.user
            form=form.save(commit=False)
            form.salary=salary
            form.experience=experience
            form.uploaded_by=user
            form.uploaded_at=timezone.now()
            if publish:
                form.published_at=timezone.now()
            form.save()
            job = Job.objects.last()
            for skill in skills:
                Skill.objects.create(name=skill, job=job)
            messages.success(request, "Job uploaded successfully")
            return redirect(".")
        else:
            messages.warning(request, "No valid data")
    else:
        form = CreateJobForm()
    return render(request, 'dashboard/create_job.html', {'form': form})

@method_decorator(allow_access_to([User.ADMIN, User.MANAGER]), name="dispatch")
class JobList(ListView):
    template_name = 'dashboard/job_list.html'
    context_object_name = 'job'
    paginate_by = 10
    
    def get_queryset(self):
        query = self.request.GET.get('name')
        sorting_value = self.request.GET.get('sorting_value')
        job = Job.objects.all_job_lists(query, sorting_value)
        if query is not None:
            job_length = len(job)
            messages.success(self.request, f"{job_length if job_length >=1  else 'No'} items found for {query}.")
        return job

job_list=JobList.as_view()

@allow_access_to([User.ADMIN, User.MANAGER])
def job_detail(request, slug):
    job = Job.objects.job_detail(slug)
    return render(request, 'dashboard/job_detail.html', {'job':job})

@allow_access_to([User.ADMIN, User.MANAGER])
def update_job(request, slug):
    job = get_object_or_404(Job, slug=slug)
    # if request.method == "POST":
    #     data=request.POST
    #     job.job_title=data['job_title']
    #     job.job_description=data['job_description']
    #     job.skills=data['skills']
    #     job.experience=data['experience']
    #     job.no_of_openings=data['no_of_openings']
    #     job.state=data['state']
    #     job.city=data['city']
    #     if data.get('publish', None)=='on':
    #         job.publish=True
    #     else:
    #         job.publish=False
    #     job.save()
    #     messages.success(request, "job updated successfully")
    #     return redirect(job.get_absolute_update_url())
    # return render(request, 'dashboard/update_job.html', {'job': job})
    if request.method == "POST":
        form = CreateJobForm(request.POST, instance=job)
        skills = request.POST.getlist('skills')
        if form.is_valid():
            publish = form.cleaned_data.get('publish')
            user=request.user
            form=form.save(commit=False)
            form.uploaded_by=user
            form.uploaded_at=timezone.now()
            if publish:
                form.published_at=timezone.now()
            form.save()
            Skill.objects.filter(job=job).delete()
            for skill in skills:
                Skill.objects.create(name=skill, job=job)
            messages.success(request, "Job updated successfully")
            return redirect(job.get_absolute_update_url())
        else:
            messages.warning(request, "No valid data")
    else:
        form = CreateJobForm(instance=job)
    return render(request, 'dashboard/update_job.html', {'form': form, 'job':job})

@method_decorator(allow_access_to([User.ADMIN, User.MANAGER]), name="dispatch")
class DeleteJob(DeleteView):
    model = Job
    success_url = reverse_lazy('dashboard:job_list')
    template_name = "dashboard/delete.html"
delete_job=DeleteJob.as_view()

@allow_access_to([User.ADMIN, User.MANAGER])
def publish_job(request, slug):
    job = get_object_or_404(Job, slug=slug)
    job.publish=True
    job.published_at=timezone.now()
    job.save()
    messages.success(request, "Published successfully")
    return redirect(request.META.get('HTTP_REFERER'))

@allow_access_to([User.ADMIN, User.MANAGER])
def unpublish_job(request, slug):
    job = get_object_or_404(Job, slug=slug)
    job.publish=False
    job.published_at=None
    job.save()
    messages.success(request, "Unpublished successfully")
    return redirect(request.META.get('HTTP_REFERER'))

@method_decorator(allow_access_to([User.ADMIN, User.MANAGER]), name="dispatch")
class ApplicantList(ListView):
    model= JobApplicant
    template_name= 'dashboard/applicant_list.html'
    context_object_name = 'applicant_list'
    paginate_by = 10
applicant_list = ApplicantList.as_view()

@allow_access_to([User.ADMIN, User.MANAGER])
def create_skillset(request):
    if request.method == "POST":
        form = AddSkillset(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Skillset added successfully")
    form = AddSkillset()
    return render(request, 'dashboard/create_skillset.html', {'form':form})

@method_decorator(allow_access_to([User.ADMIN, User.MANAGER]), name="dispatch")
class SkillsetList(ListView):
    model = SkillSet
    template_name = 'dashboard/skillset_list.html'
    context_object_name = 'skillsets'
    paginate_by = 8
    
    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get('name')
        sorting_value = self.request.GET.get('sorting_value')
        skillsets = SkillSet.objects.skillset_lists(query, sorting_value)
        if query is not None:
            skillsets_length = len(skillsets)
            messages.success(self.request, f"{skillsets_length if skillsets_length >=1  else 'No'} items found for {query}.")
        return skillsets
skillset_list = SkillsetList.as_view()

@allow_access_to([User.ADMIN, User.MANAGER])
def skillset_detail(request, pk):
    skillset = SkillSet.objects.skillset_detail(pk)
    return render(request, 'dashboard/skillset_detail.html', {'skillset':skillset})

allow_access_to([User.ADMIN, User.MANAGER])
def update_skillset(request, pk):
    skillset = get_object_or_404(SkillSet, pk=pk)
    form = AddSkillset(request.POST, instance=skillset)
    if form.is_valid():
        form.save()
        messages.success(request, "Skillset added successfully")

    form = AddSkillset(instance=skillset)
    return render(request, 'dashboard/update_skillset.html', {'form':form})

@method_decorator(allow_access_to([User.ADMIN, User.MANAGER]), name="dispatch")
class DeleteSkillset(DeleteView):
    model = SkillSet
    success_url = reverse_lazy('dashboard:skillset_list')
    template_name = "dashboard/skillset_confirm_delete.html"
delete_skillset=DeleteSkillset.as_view()

@allow_access_to([User.ADMIN, User.MANAGER])
def export_applicant_list(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="applicants.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Applicants')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ('Name', 
               'Mobile', 
               'Email Address', 
               'Notice period', 
               'LinkedIn link', 
               'Qualitative skills', 
               'Subject', 
               'message'
    )
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = JobApplicant.objects.values_list('user__name', 
                                            'user__mobile', 
                                            'user__email', 
                                            'notice_period', 
                                            'linkedin_link', 
                                            'qualitative_skills', 
                                            'subject', 
                                            'message'
                                            )
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response