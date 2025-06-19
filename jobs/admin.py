from django.contrib import admin
from .models import Job, JobApplication, Review, JobCategory

@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'employer', 'job_type', 'schedule', 'salary', 'location', 'is_active')
    list_filter = ('job_type', 'schedule', 'is_active')
    search_fields = ('title', 'description', 'location')
    raw_id_fields = ('employer', 'category')

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'worker', 'status', 'applied_at')
    list_filter = ('status',)
    search_fields = ('job__title', 'worker__username')
    raw_id_fields = ('job', 'worker')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'reviewed_user', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('reviewer__username', 'reviewed_user__username')
    raw_id_fields = ('reviewer', 'reviewed_user', 'job')