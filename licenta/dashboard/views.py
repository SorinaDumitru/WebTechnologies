
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserLoginForm

def about(request):
    return render(request, 'dashboard/about-us.html', {'title': 'About'})


def homepage(request):
    print("FOOOOOOOOOOOOOOOOOOOOOOOO")
    if request.method == 'POST':
        print("POSTTTTTTTTTTTTTTTTTT")

        form = UserLoginForm(request)

        # if form.is_valid():
        print("VALID FORM")
        form.save()
        messages.success(request, f'Login done?')
        return redirect('profile')

    else:
        form = UserLoginForm(request)

    if request.user and request.user.is_authenticated:
        return render(request, 'users/profile.html')
    return render(request, 'dashboard/home.html', {"form": form})


# def homepage(request):
#     return render(request, 'dashboard/home.html', {'title': 'homepage', 'app_name': 'dogtor'})


def contact(request):
    return render(request, 'dashboard/contact.html', {'title': 'contact'})


def dashboard(request):
    return render(request, 'dashboard/dashboard.html', {'title': 'Dashboard'})


def form_base(request):
    return render(request, 'dashboard/form-base.html', {'title': 'Form Base'})

# def contactView(request):
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject, message, email, [settings.EMAIL_HOST_USER, email])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')

#             messages.success(request, f'Email sent successfully!')
#             return redirect('dashboard-contact')
#     return render(request, "dashboard/contact.html", {'form': form})
