from django.db import models
from django.contrib.postgres.search import (
                                        SearchVector, 
                                        SearchQuery, 
                                        SearchHeadline,
                                        SearchRank
                                    )

class JobQuerySet(models.QuerySet):

    def search(self, query, queryset):
        vector = SearchVector('job_title', 'job_description', 'place')
        query = SearchQuery(query)
        search_headline = SearchHeadline('job_description', query)
        queryset = queryset.annotate(
                        rank=SearchRank
                        (vector, query)
                        ).annotate(
                        headline=search_headline
                        ).filter(
                        rank__gte=0.001
                        ).order_by(
                        '-rank'
                        )
        return queryset
    
    def all_job_lists(self, query, sorting_value):
        queryset = self.all().order_by("-id")
        if sorting_value is not None:
            queryset=queryset.order_by(sorting_value)
        if query is None:
            return queryset
        else:
            return self.search(query, queryset)
        
    def published_job_lists(self, query):
        queryset = self.filter(publish=True).order_by("-id")
        if query is None:
            return queryset
        else:
            return self.search(query, queryset)

    def unpublished_job_lists(self):
        return self.filter(publish=False)

    def job_detail(self, slug):
        return self.get(slug=slug)

    def update_job(self, slug):
        self.get(slug=slug)
    
class JobManager(models.Manager):
    def get_queryset(self):
        return JobQuerySet(self.model, using=self._db)
    
    def all_job_lists(self, query, sorting_value):
        return self.get_queryset().all_job_lists(query, sorting_value)
    
    def published_job_lists(self, query=None):
        return self.get_queryset().published_job_lists(query)
        
    def unpublished_job_lists(self):
        return self.get_queryset().unpublished_job_lists()

    def job_detail(self, slug):
        return self.get_queryset().job_detail(slug)


class JobApplicantQuerySet(models.QuerySet):

    def search(self, query, queryset):
        vector = SearchVector('user__name', 'user__mobile', 'user__email', 'notice_period')
        query = SearchQuery(query)
        search_headline = SearchHeadline('user__email', query)
        queryset = queryset.annotate(
                        rank=SearchRank
                        (vector, query)
                        ).annotate(
                        headline=search_headline
                        ).filter(
                        rank__gte=0.001
                        ).order_by(
                        '-rank'
                        )
        return queryset
    
    def all_applicant_lists(self, query, sorting_value):
        queryset = self.all()
        if sorting_value is not None:
            queryset=queryset.order_by(sorting_value)
        if query is None:
            return queryset
        else:
            return self.search(query, queryset)
    
class JobApplicantManager(models.Manager):
    def get_queryset(self):
        return JobApplicantQuerySet(self.model, using=self._db)
    
    def all_applicant_lists(self, query, sorting_value):
        return self.get_queryset().all_applicant_lists(query, sorting_value)