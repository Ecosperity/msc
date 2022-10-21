from django.contrib import messages
from hitcount.views import HitCountDetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.db import transaction
from django.http import JsonResponse
from django.views.generic import ListView
from django.core.cache import cache
from apps.job.forms import JobApplicantForm, JobApplicantUserForm
from job.models import Job, JobApplicant, Skill
from dashboard.models import SkillSet
import logging
User = get_user_model()

@csrf_exempt
def search(request):
    if request.is_ajax and request.method == "GET":
        if 'term' in request.GET:
            term = request.GET.get("term")
            skill_queryset = Skill.objects.filter(Q(name__icontains=term))
            job_queryset = Job.objects.filter(Q(job_title__icontains=term))
    
            skill_query = [query.name for query in skill_queryset]
            job_query =[query.job_title for query in job_queryset]
            list_queryset = skill_query + job_query
        if 'location' in request.GET:
            location = request.GET.get("location")
            queryset = Job.objects.filter(Q(place__icontains=location))
            list_queryset = [query.place for query in queryset] 

        unique_list_queryset = list(dict.fromkeys(list_queryset))
        return JsonResponse(unique_list_queryset, safe=False)   

class HomeView(ListView):
    model = Job
    template_name = 'templates/index.html'
    context_object_name = 'jobs'
    def get_queryset(self, *args, **kwargs):
        objects = cache.get('objects')
        if objects is None:
            objects = Job.objects.published_job_lists().order_by("-published_at", "-id")[:5]
            cache.set('objects', objects)
        return objects

class JobList(ListView):
    model = Job
    template_name = 'job/job_list.html'
    context_object_name = 'jobs'
    paginate_by = 12
    
    def get_queryset(self):
        locations = self.request.GET.get('locations')
        skills = self.request.GET.get('skills')

        object_list = cache.get('object_list')
        if object_list is None:
            object_list = Job.objects.published_job_lists()
            cache.set('object_list', object_list)

        if locations or skills:
            location_lists = [location_list.strip(' ') for location_list in [location for location in locations.split(",") if location!=" "]]
            skill_lists = [skill_list.strip(' ') for skill_list in [skill for skill in skills.split(",") if skill!=" "]]
            search_skills = location_lists + skill_lists
            object_list = Job.objects.published_job_lists(search_skills)        
            job_length = len(object_list)
            if job_length < 1 :
                object_list = Job.objects.published_job_lists()
                messages.success(self.request, "No job found.")
            else:
                messages.success(self.request, f"{job_length} Job found.")
        return object_list
job_list = JobList.as_view()

@method_decorator(login_required, name='dispatch')
class JobDetail(HitCountDetailView):
    model = Job
    template_name = "job/job_detail.html"
    context_object_name = "job"
    slug_field = 'slug'
    count_hit = True

    def get_queryset(self):
        slug=self.kwargs.get('slug')
        object = cache.get('object')
        if object is None:
            object = Job.objects.filter(slug=slug)
            cache.set('object', object)
        return object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user=self.request.user
        slug=self.kwargs.get('slug')
        skill=[skill.name for skill in self.object.skill_set.all()]
        object=self.object
        context['check_applied_condition'] = 1 in [job.is_applied for job in Job.objects.get(slug=slug).jobapplicant_set.all().filter(user=user)]
        context['similar_jobs'] = cache.get('similar_jobs')
        if context['similar_jobs'] is None:
            context['similar_jobs'] = Job.objects.filter(country=object.country, place=object.place, skill__name__in=skill).distinct().exclude(slug=slug)
            cache.set('similar_jobs', context['similar_jobs'])

        try:
            applicant = JobApplicant.objects.get(user=user)
        except:
            applicant=None
        context['user_form'] = JobApplicantUserForm(instance=user)
        context['applicant_form'] = JobApplicantForm(instance=applicant)
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
        user_form = JobApplicantUserForm(request.POST, request.FILES, instance=user)
        applicant_form = JobApplicantForm(request.POST, request.FILES, instance=applicant)
        if user_form.is_valid() and applicant_form.is_valid():
            resume=applicant_form.cleaned_data.get('resume')
            if resume.size > 2 * 1024 * 1024:
                logging.warning("Applicant attempted to upload large resume file.")
                messages.warning(request, "Resume too large. Size should not exceed 2 MiB.")
                return redirect("job:job_detail", slug=job.slug)

            notice_period=applicant_form.cleaned_data.get('notice_period')
            resume=applicant_form.cleaned_data.get('resume')
            name=user_form.cleaned_data.get('name')
            mobile=user_form.cleaned_data.get('mobile')

            linkedin_link=applicant_form.cleaned_data.get('linkedin_link')
            qualitative_skills=applicant_form.cleaned_data.get('qualitative_skills')
            subject=applicant_form.cleaned_data.get('subject')
            message=applicant_form.cleaned_data.get('message')
            try:
                with transaction.atomic():
                    user.name=name
                    user.mobile=mobile
                    user.save()
                    try:
                        applicant = JobApplicant.objects.get(user=user)
                        applicant.notice_period=notice_period
                        applicant.resume=resume
                        applicant.linkedin_link=linkedin_link
                        applicant.qualitative_skills=qualitative_skills
                        applicant.subject=subject
                        applicant.message=message
                    except:
                        applicant = JobApplicant(
                                    user=user,
                                    notice_period=notice_period,
                                    is_applied=1,
                                    resume=resume,
                                    linkedin_link=linkedin_link,
                                    qualitative_skills=qualitative_skills,
                                    subject=subject,
                                    message=message,
                                )
                    applicant.save()
                    applicant.job.add(job)
                    job.job_applied_count=job.job_applied_count + 1 if job.job_applied_count else 1
                    job.save()
                    messages.success(request, "You have succesfully applied for the job")
                    return redirect("job:job_detail", slug=job.slug)
            except:
                logging.info("Some error occured while applying the job")
                messages.warning(request, "Not able to apply, please try again")
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.warning(request, "Something went wrong or not valid data")
            return redirect("job:job_detail", slug=job.slug)

@csrf_exempt
def skillSearch(request):
    if request.is_ajax and request.method == "GET":
        if 'term' in request.GET:
            term = request.GET.get("term")           
            list_queryset = SkillSet.objects.filter(name__icontains=term)
            list_queryset = [query.name for query in list_queryset]
            return JsonResponse(list_queryset, safe=False)

def search_result(request):
    salary = request.GET.get("salary", None)
    freshness = request.GET.get("freshness", None)
    experience = request.GET.get("experience", None)
    country = request.GET.getlist("country", None)
    job_list = Job.objects.get_filtered_data(salary, freshness, experience, country)
    
    context = {'job_list':job_list,
               'freshness':freshness,
               'salary':salary,
               'experience':experience,
               }
    return render(request, 'job/search_result.html', context)