from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django_filters.views import FilterView
from .models import Job, JobApplication, Review, JobCategory
from .filters import JobFilter
from .forms import JobForm, JobApplicationForm, ReviewForm

class JobListView(FilterView):
    model = Job
    template_name = 'jobs/job_list.html'
    filterset_class = JobFilter
    paginate_by = 10
    context_object_name = 'jobs'
    
    def get_queryset(self):
        return Job.objects.filter(is_active=True).order_by('-created_at')

class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/job_detail.html'
    context_object_name = 'job'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated and self.request.user.is_worker:
            context['has_applied'] = JobApplication.objects.filter(
                job=self.object, 
                worker=self.request.user
            ).exists()
        return context

class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/job_form.html'
    
    def form_valid(self, form):
        form.instance.employer = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('job_detail', kwargs={'pk': self.object.pk})

class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/job_form.html'
    
    def get_success_url(self):
        return reverse_lazy('job_detail', kwargs={'pk': self.object.pk})

def apply_for_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.worker = request.user
            application.save()
            messages.success(request, 'Ваша заявка успешно отправлена!')
            return redirect('job_detail', pk=job.pk)
    else:
        form = JobApplicationForm()
    return render(request, 'jobs/apply_for_job.html', {'form': form, 'job': job})

class DashboardView(LoginRequiredMixin, ListView):
    template_name = 'jobs/dashboard.html'
    context_object_name = 'applications'
    
    def get_queryset(self):
        if self.request.user.is_worker:
            return JobApplication.objects.filter(worker=self.request.user).order_by('-applied_at')
        else:
            return JobApplication.objects.filter(job__employer=self.request.user).order_by('-applied_at')

class EmployerDashboardView(LoginRequiredMixin, ListView):
    template_name = 'jobs/employer_dashboard.html'
    context_object_name = 'jobs'
    
    def get_queryset(self):
        return Job.objects.filter(employer=self.request.user).order_by('-created_at')

def create_review(request, user_id):
    reviewed_user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.reviewed_user = reviewed_user
            review.save()
            messages.success(request, 'Ваш отзыв успешно сохранен!')
            return redirect('profile', user_id=reviewed_user.pk)
    else:
        form = ReviewForm()
    return render(request, 'jobs/review_form.html', {'form': form, 'reviewed_user': reviewed_user})