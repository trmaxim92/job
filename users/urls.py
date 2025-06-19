from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('profile/<int:user_id>/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('register/', views.register, name='register'),
]