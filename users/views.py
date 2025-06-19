from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileEditForm
from .models import CustomUser

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен!')
            return redirect('profile', user_id=request.user.id)
    else:
        form = ProfileEditForm(instance=request.user)
    
    return render(request, 'users/profile_edit.html', {'form': form})

def profile_view(request, user_id):
    user_profile = get_object_or_404(CustomUser, pk=user_id)
    user_review = None
    
    if request.user.is_authenticated and request.user != user_profile:
        user_review = Review.objects.filter(
            reviewer=request.user,
            reviewed_user=user_profile
        ).first()
    
    return render(request, 'users/profile.html', {
        'user_profile': user_profile,
        'user_review': user_review
    })


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})