from django.urls import path
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import reverse
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.Settings.as_view(), name='settings'),
    path('email_change/', views.SettingsChange.as_view(fields=['email']), name='email_change'),
    path('username_change/', views.SettingsChange.as_view(fields=['username']), name='username_change'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
