from django.db import models


class SkillSet(models.Model):
    name = models.CharField(max_length=50)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name