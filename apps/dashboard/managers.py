from django.db import models
from django.shortcuts import get_object_or_404
from django.db.models import Q

class SkillSetQuerySet(models.QuerySet):
    
    def search(self, query, queryset):
        queryset = queryset.filter(Q(name=query))
        return queryset

    def skillset_lists(self, query, sorting_value):
        queryset = self.all()
        if sorting_value is not None:
            queryset=queryset.order_by(sorting_value)
        if query is None:
            return queryset
        else:
            return self.search(query, queryset)
        
    def skillset_detail(self, pk):
        return get_object_or_404(self, pk=pk)
        
class SkillSetManager(models.Manager):
    def get_queryset(self):
        return SkillSetQuerySet(self.model, using=self._db)
    
    def skillset_lists(self, query, sorting_value):
        return self.get_queryset().skillset_lists(query, sorting_value)
    
    def skillset_detail(self, pk):
        return self.get_queryset().skillset_detail(pk)
    