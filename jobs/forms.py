from django import forms
from .models import Job, JobApplication, Review
from allauth.account.forms import SignupForm

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'title', 'description', 'category', 'job_type', 'schedule', 
            'payment_type', 'salary', 'location', 'latitude', 'longitude'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'location': forms.TextInput(attrs={
                'id': 'location-input',
                'placeholder': 'Введите адрес'
            }),
        }

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Напишите сопроводительное письмо (не обязательно)'
            }),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment', 'job']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
            'job': forms.HiddenInput(),
        }
