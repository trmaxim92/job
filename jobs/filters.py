import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    salary_min = django_filters.NumberFilter(field_name='salary', lookup_expr='gte')
    salary_max = django_filters.NumberFilter(field_name='salary', lookup_expr='lte')
    
    class Meta:
        model = Job
        fields = {
            'job_type': ['exact'],
            'schedule': ['exact'],
            'payment_type': ['exact'],
            'category': ['exact'],
        }