from django import forms
from job.models import Job

class CreateJobForm(forms.ModelForm):
    job_title = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control'}))
    job_description = forms.CharField(widget=forms.Textarea( attrs={'class': 'form-control','rows':5,}))
    skills = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    no_of_openings = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}), max_length=500)
    experience = forms.ChoiceField(widget=forms.Select( attrs={'class': 'form-control'}), choices=Job.EMPLOYEE_EXPERIENCE_TYPE_CHOICES,  required=True)
    class Meta:
        model = Job
        fields = "__all__"
        exclude = ('slug', 
                   'uploaded_by', 
                   'published_at', 
                   'employement_type', 
                   'visit_count', 
                   'updated_at', 
                   'job_applied_count'
                   )