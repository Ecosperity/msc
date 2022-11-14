from django.db import models
from dashboard.managers import SkillSetManager
from django.urls import reverse

class SkillSet(models.Model):
    name = models.CharField(max_length=50)
    added = models.DateTimeField(auto_now_add=True)

    objects = SkillSetManager()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("dashboard:skillset_detail", kwargs={"pk": self.pk}) 
    
    def get_absolute_update_url(self):
        return reverse("dashboard:update_skillset", kwargs={"pk": self.pk}) 

    def get_absolute_delete_url(self):
            return reverse("dashboard:delete_skillset", kwargs={"pk": self.pk}) 
