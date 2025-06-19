from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator

User = get_user_model()

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'profile_picture', 'about']
        widgets = {
            'about': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_picture'].validators = [
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])
        ]
        self.fields['profile_picture'].required = False