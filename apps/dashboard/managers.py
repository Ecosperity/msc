from django.db import models
from django.contrib.postgres.search import (
                                        SearchVector, 
                                        SearchQuery, 
                                        SearchHeadline,
                                        SearchRank
                                    )
from django.shortcuts import get_object_or_404

class SkillSetQuerySet(models.QuerySet):
    
    def search(self, query, queryset):
        vector = SearchVector('name')
        query = SearchQuery(query)
        search_headline = SearchHeadline('name', query)
        return queryset.annotate(
                        rank=SearchRank
                        (vector, query)
                        ).annotate(
                        headline=search_headline
                        ).filter(
                        rank__gte=0.001
                        ).order_by(
                        '-rank'
                        )

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
    