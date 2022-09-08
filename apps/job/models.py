from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from .utils import generate_unique_slug
from django.urls import reverse
from job.managers import JobManager
from django.db.models.functions import Cast
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

    EMPLOYEE_EXPERIENCE_FRESHER = 'Fresher (less than one year)'
    EMPLOYEMENT_EXPERIENCE_ONE_YEAR = '1 year'
    EMPLOYEMENT_EXPERIENCE_TWO_YEARS = '2 years'
    EMPLOYEMENT_EXPERIENCE_THREE_YEARS = '3 years'
    EMPLOYEMENT_EXPERIENCE_FOUR_YEARS = '4 years'
    EMPLOYEMENT_EXPERIENCE_FIVE_YEARS = '5 years'
    EMPLOYEMENT_EXPERIENCE_SIX_YEARS = '6 years'
    EMPLOYEMENT_EXPERIENCE_SEVEN_YEARS = '7 years'
    EMPLOYEMENT_EXPERIENCE_EIGHT_YEARS = '8 years'
    EMPLOYEMENT_EXPERIENCE_NINE_YEARS = '9 years'
    EMPLOYEMENT_EXPERIENCE_TEN_YEARS = '10 years'
    EMPLOYEMENT_EXPERIENCE_ELEVEN_YEARS = '11 years'
    EMPLOYEMENT_EXPERIENCE_TWELVE_YEARS = '12 years'
    EMPLOYEMENT_EXPERIENCE_THIRTEEN_YEARS = '13 years'
    EMPLOYEMENT_EXPERIENCE_FOURTEEN_YEARS = '14 years'
    EMPLOYEMENT_EXPERIENCE_FIFTEEN_YEARS = '15 years'
    EMPLOYEMENT_EXPERIENCE_SIXTEEN_YEARS = '16 years'
    EMPLOYEMENT_EXPERIENCE_SEVENTEEN_YEARS = '17 years'
    EMPLOYEMENT_EXPERIENCE_EIGHTEEN_YEARS = '18 years'
    EMPLOYEMENT_EXPERIENCE_NINETEEN_YEARS = '19 years'
    EMPLOYEMENT_EXPERIENCE_TWENTY_YEARS = '20 years'
    EMPLOYEMENT_EXPERIENCE_TWENTY_ONE_YEARS = '21 years'
    EMPLOYEMENT_EXPERIENCE_TWENTY_TWO_YEARS = '22 years'
    EMPLOYEMENT_EXPERIENCE_TWENTY_THREE_YEARS = '23 years'
    EMPLOYEMENT_EXPERIENCE_TWENTY_FOUR_YEARS = '24 years'
    EMPLOYEMENT_EXPERIENCE_TWENTY_FIVE_YEARS = '25 years'
    EMPLOYEMENT_EXPERIENCE_TWENTY_SIX_YEARS = '26 years'
    EMPLOYEMENT_EXPERIENCE_TWENTY_SEVEN_YEARS = '27 years'
    EMPLOYEMENT_EXPERIENCE_TWENTY_EIGHT_YEARS = '28 years'
    EMPLOYEMENT_EXPERIENCE_TWENTY_NINE_YEARS = '29 years'
    EMPLOYEMENT_EXPERIENCE_THIRTY_YEARS = '30 years'

    EMPLOYEE_EXPERIENCE_TYPE_CHOICES= (
        (EMPLOYEE_EXPERIENCE_FRESHER, EMPLOYEE_EXPERIENCE_FRESHER),
        (EMPLOYEMENT_EXPERIENCE_ONE_YEAR, EMPLOYEMENT_EXPERIENCE_ONE_YEAR),
        (EMPLOYEMENT_EXPERIENCE_TWO_YEARS, EMPLOYEMENT_EXPERIENCE_TWO_YEARS),
        (EMPLOYEMENT_EXPERIENCE_THREE_YEARS, EMPLOYEMENT_EXPERIENCE_THREE_YEARS),
        (EMPLOYEMENT_EXPERIENCE_FOUR_YEARS, EMPLOYEMENT_EXPERIENCE_FOUR_YEARS),
        (EMPLOYEMENT_EXPERIENCE_FIVE_YEARS, EMPLOYEMENT_EXPERIENCE_FIVE_YEARS),
        (EMPLOYEMENT_EXPERIENCE_SIX_YEARS, EMPLOYEMENT_EXPERIENCE_SIX_YEARS),
        (EMPLOYEMENT_EXPERIENCE_SEVEN_YEARS, EMPLOYEMENT_EXPERIENCE_SEVEN_YEARS),
        (EMPLOYEMENT_EXPERIENCE_EIGHT_YEARS, EMPLOYEMENT_EXPERIENCE_EIGHT_YEARS),
        (EMPLOYEMENT_EXPERIENCE_NINE_YEARS, EMPLOYEMENT_EXPERIENCE_NINE_YEARS),
        (EMPLOYEMENT_EXPERIENCE_TEN_YEARS, EMPLOYEMENT_EXPERIENCE_TEN_YEARS),
        (EMPLOYEMENT_EXPERIENCE_ELEVEN_YEARS, EMPLOYEMENT_EXPERIENCE_ELEVEN_YEARS),
        (EMPLOYEMENT_EXPERIENCE_TWELVE_YEARS, EMPLOYEMENT_EXPERIENCE_TWELVE_YEARS),
        (EMPLOYEMENT_EXPERIENCE_THIRTEEN_YEARS, EMPLOYEMENT_EXPERIENCE_THIRTEEN_YEARS),
        (EMPLOYEMENT_EXPERIENCE_FOURTEEN_YEARS, EMPLOYEMENT_EXPERIENCE_FOURTEEN_YEARS),
        (EMPLOYEMENT_EXPERIENCE_FIFTEEN_YEARS, EMPLOYEMENT_EXPERIENCE_FIFTEEN_YEARS),
        (EMPLOYEMENT_EXPERIENCE_SIXTEEN_YEARS, EMPLOYEMENT_EXPERIENCE_SIXTEEN_YEARS),
        (EMPLOYEMENT_EXPERIENCE_SEVENTEEN_YEARS, EMPLOYEMENT_EXPERIENCE_SEVENTEEN_YEARS),
        (EMPLOYEMENT_EXPERIENCE_EIGHTEEN_YEARS, EMPLOYEMENT_EXPERIENCE_EIGHTEEN_YEARS),
        (EMPLOYEMENT_EXPERIENCE_NINETEEN_YEARS, EMPLOYEMENT_EXPERIENCE_NINETEEN_YEARS),
        (EMPLOYEMENT_EXPERIENCE_TWENTY_YEARS, EMPLOYEMENT_EXPERIENCE_TWENTY_YEARS),
        (EMPLOYEMENT_EXPERIENCE_TWENTY_ONE_YEARS, EMPLOYEMENT_EXPERIENCE_TWENTY_ONE_YEARS),
        (EMPLOYEMENT_EXPERIENCE_TWENTY_TWO_YEARS, EMPLOYEMENT_EXPERIENCE_TWENTY_TWO_YEARS),
        (EMPLOYEMENT_EXPERIENCE_TWENTY_THREE_YEARS, EMPLOYEMENT_EXPERIENCE_TWENTY_THREE_YEARS),
        (EMPLOYEMENT_EXPERIENCE_TWENTY_FOUR_YEARS, EMPLOYEMENT_EXPERIENCE_TWENTY_FOUR_YEARS),
        (EMPLOYEMENT_EXPERIENCE_TWENTY_FIVE_YEARS, EMPLOYEMENT_EXPERIENCE_TWENTY_FIVE_YEARS),
        (EMPLOYEMENT_EXPERIENCE_TWENTY_SIX_YEARS, EMPLOYEMENT_EXPERIENCE_TWENTY_SIX_YEARS),
        (EMPLOYEMENT_EXPERIENCE_TWENTY_SEVEN_YEARS, EMPLOYEMENT_EXPERIENCE_TWENTY_SEVEN_YEARS),
        (EMPLOYEMENT_EXPERIENCE_TWENTY_EIGHT_YEARS, EMPLOYEMENT_EXPERIENCE_TWENTY_EIGHT_YEARS),
        (EMPLOYEMENT_EXPERIENCE_TWENTY_NINE_YEARS, EMPLOYEMENT_EXPERIENCE_TWENTY_NINE_YEARS),
        (EMPLOYEMENT_EXPERIENCE_THIRTY_YEARS, EMPLOYEMENT_EXPERIENCE_THIRTY_YEARS),
    )

    job_title = models.CharField(max_length=50)
    job_description = models.TextField()
    slug = models.SlugField(max_length=60, blank=True, null=True)
    employement_type = models.CharField(max_length=50, 
                                        choices=EMPLOYEMENT_TYPE_CHOICES, 
                                        default=EMPLOYEMENT_TYPE_FULL_TIME
                                        )
    experience = models.CharField(max_length=50, 
                                  choices=EMPLOYEE_EXPERIENCE_TYPE_CHOICES
                                  )
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, blank=True)
    no_of_openings = models.PositiveSmallIntegerField()
    visit_count = models.PositiveIntegerField(default=0)
    job_applied_count = models.PositiveIntegerField(default=0)

    skills = models.CharField(max_length=50)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    publish = models.BooleanField(default=False)
    # dates
    uploaded_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    
    objects = JobManager()

    class Meta:
        verbose_name = _('Job Post')
        verbose_name_plural = _('Job Posts')
        ordering = ["-publish", "-published_at", Cast("visit_count", output_field=models.IntegerField()),]

    def save(self, *args, **kwargs):
        if self.slug:
            if slugify(self.job_title) != self.slug:
                self.slug = generate_unique_slug(Job, self.job_title)
        else: 
            self.slug = generate_unique_slug(Job, self.job_title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.job_title
    
    def get_absolute_url(self):
        return reverse("dashboard:job_detail", kwargs={"slug": self.slug}) 

    def get_absolute_update_url(self):
        return reverse("dashboard:update_job", kwargs={"slug": self.slug}) 

    def get_absolute_delete_url(self):
            return reverse("dashboard:delete_job", kwargs={"slug": self.slug}) 

