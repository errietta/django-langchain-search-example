from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.JobListAPI.as_view(), name='job_list_api'),
    path('schools/', views.SchoolListAPI.as_view(), name='school_list_api'),
]
