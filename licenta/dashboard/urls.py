from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.homepage, name='dashboard-homepage'),
    path('about/', views.about, name='dashboard-about'),
    path('contact/', views.contact, name='dashboard-contact'),
    path('dashboard/', views.dashboard, name="dashboard-dashboard"),
    path('form-base/', views.form_base, name="dashboard-form-base"),
]
