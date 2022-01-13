from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm #, UserLoginForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}!')
            return redirect('dashboard-homepage')
    else:
        form = UserRegisterForm()

    return render(request, 'dashboard/home.html', {'form': form, 'title': 'Register'})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
