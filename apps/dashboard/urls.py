from django.urls import path
from . import views
app_name='dashboard'
urlpatterns=[
    path("", views.dashboard, name='dashboard'),
    path("create-job/", views.create_job, name='create_job'),
    path("job-list/", views.job_list, name='job_list'),
    path("job-detail/<slug>/", views.job_detail, name='job_detail'),
    path("update-job/<slug>/", views.update_job, name='update_job'),
    path("delete-job/<slug>/", views.delete_job, name='delete_job'),
    path("publish-job/<slug>/", views.publish_job, name='publish_job'),
    path("unpublish-job/<slug>/", views.unpublish_job, name='unpublish_job'),
    path("applicant-list/", views.applicant_list, name='applicant_list'),
    path("create-skillset/", views.create_skillset, name='create_skillset'),
    path("skillset-list/", views.skillset_list, name='skillset_list'),
    path("skillset-detail/<int:pk>/", views.skillset_detail, name='skillset_detail'),
    path("update-skillset/<int:pk>/", views.update_skillset, name='update_skillset'),
    path("delete-skillset/<int:pk>/", views.delete_skillset, name='delete_skillset'),
    path("export-applicant-list/", views.export_applicant_list, name='export_applicant_list'),
    path("toggle-recommended-jobs/<slug>/", views.toggle_recommended_jobs, name='toggle_recommended_jobs'),
]