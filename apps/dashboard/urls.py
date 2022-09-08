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
]