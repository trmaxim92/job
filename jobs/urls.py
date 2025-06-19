from django.urls import path
from .views import (
    JobListView, JobDetailView, JobCreateView, JobUpdateView,
    apply_for_job, DashboardView, EmployerDashboardView, create_review
)

app_name = 'jobs'

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('create/', JobCreateView.as_view(), name='job_create'),
    path('<int:pk>/update/', JobUpdateView.as_view(), name='job_update'),
    path('<int:pk>/apply/', apply_for_job, name='apply_for_job'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('employer-dashboard/', EmployerDashboardView.as_view(), name='employer_dashboard'),
    path('user/<int:user_id>/review/', create_review, name='create_review'),
]