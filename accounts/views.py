from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import redirect, render

from accounts.forms import ChangePasswordForm, CreationForm, EditProfileForm
from accounts.models import ExtendUser


def my_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            extend_user, is_new = ExtendUser.objects.get_or_create(user=request.user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {})

@login_required
def edit_profile(request):
    user = request.user
    
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            new_data = form.cleaned_data
            user.first_name = new_data['first_name']
            user.last_name = new_data['last_name']
            user.email = new_data['email']
            user.extenduser.avatar = new_data['avatar']
            user.extenduser.save()
            user.save()
            return redirect('profile')
    else:
        form = EditProfileForm(
            initial={
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'avatar': user.extenduser.avatar,
            }
        )
    return render(request, 'accounts/edit-profile.html', {'form': form})


class ChangePassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/change-pass.html'
    success_url = '/accounts/profile/'
    form_class = ChangePasswordForm