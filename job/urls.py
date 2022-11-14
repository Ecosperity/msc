from django.urls import path
from . import views

app_name='job'
urlpatterns=[
    path("", views.HomeView.as_view(), name='home'),
]