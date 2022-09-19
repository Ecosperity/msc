from django import forms

from dashboard.models import SkillSet

class AddSkillset(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control'}))

    class Meta:
        model = SkillSet
        fields = ("name",)