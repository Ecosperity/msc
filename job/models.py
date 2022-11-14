from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
from .managers import JobApplicantManager, JobManager
from tinymce.models import HTMLField
User=get_user_model()

class Job(models.Model):
    EMPLOYEMENT_TYPE_FULL_TIME = 'Full time'
    EMPLOYEMENT_TYPE_PART_TIME = 'Part time'
    EMPLOYEMENT_TYPE_FREELANCING = 'Freelancing'
    EMPLOYEMENT_TYPE_CONTRACT = 'Contract'

    EMPLOYEMENT_TYPE_CHOICES = (
        (EMPLOYEMENT_TYPE_FULL_TIME, EMPLOYEMENT_TYPE_FULL_TIME),
        (EMPLOYEMENT_TYPE_PART_TIME, EMPLOYEMENT_TYPE_PART_TIME),
        (EMPLOYEMENT_TYPE_FREELANCING, EMPLOYEMENT_TYPE_FREELANCING),
        (EMPLOYEMENT_TYPE_CONTRACT, EMPLOYEMENT_TYPE_CONTRACT),
    )

    INDIA = 'India'
    ITALY = 'Italy'
    SWITZERLAND = 'Switzerland'
    USA = 'USA'

    COUNTRY_CHOICES = (
        (INDIA, INDIA),
        (ITALY, ITALY),
        (SWITZERLAND, SWITZERLAND),
        (USA, USA),
    )

    slug = models.SlugField(max_length=100, blank=True, null=True)
    job_title = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    job_description = HTMLField() 
    experience = models.CharField(max_length=50)
    salary = models.CharField(max_length=50, blank=True, null=True)
    no_of_openings = models.PositiveSmallIntegerField()
    industry = models.CharField(max_length=100)
    functional_area = models.CharField(max_length=100)
    employement_type = models.CharField(max_length=50, 
                                        choices=EMPLOYEMENT_TYPE_CHOICES, 
                                        default=EMPLOYEMENT_TYPE_FULL_TIME
                                        )
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES)
    place = models.CharField(max_length=50, blank=True)
    visit_count = models.PositiveIntegerField(default=0)
    job_applied_count = models.PositiveIntegerField(default=0)

    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    publish = models.BooleanField(default=False)
    recommended_job = models.BooleanField(default=False)
    # dates
    uploaded_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    
    objects = JobManager()

    class Meta:
        verbose_name = _('Job Post')
        verbose_name_plural = _('Job Posts')

    # def save(self, *args, **kwargs):
    #     if self.slug:
    #         if slugify(self.job_title) != self.slug:
    #             self.slug = generate_unique_slug(Job, self.job_title, self)
    #     else: 
    #         self.slug = generate_unique_slug(Job, self.job_title)
    #     super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.job_title
    
    def get_absolute_url(self):
        return reverse("dashboard:job_detail", kwargs={"slug": self.slug}) 
    
    def get_applicant_absolute_url(self):
        return reverse("job:job_detail", kwargs={"slug": self.slug}) 

    def get_absolute_update_url(self):
        return reverse("dashboard:update_job", kwargs={"slug": self.slug}) 

    def get_absolute_delete_url(self):
            return reverse("dashboard:delete_job", kwargs={"slug": self.slug}) 

class Skill(models.Model):
    name = models.CharField(max_length=50)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
class JobApplicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="applicant_user")
    job = models.ManyToManyField(Job)
    is_applied = models.BooleanField(default=False)
    notice_period = models.CharField(max_length=20)
    linkedin_link = models.URLField(max_length=100)
    qualitative_skills = models.CharField(max_length=100)
    resume = models.FileField(upload_to="resumes/%Y/%m/%d/")
    subject = models.CharField(max_length=200)
    message = models.TextField()

    objects = JobApplicantManager()

    def __str__(self):
        return f'Applicantt ==> {self.user}'

