from django.urls import reverse_lazy
from django.views import generic
from customuser.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages

from customuser.models import User


# Create your views here.

class SettingsChange(LoginRequiredMixin, generic.UpdateView):
    model = User
    template_name = 'accounts/settings_change.html'
    success_url = reverse_lazy('accounts:settings')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Your settings were changed.')
        return super().form_valid(form)


class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy('accounts:settings')

    def form_valid(self, form):
        messages.success(self.request, 'Your password was changed.')
        return super().form_valid(form)


class Settings(LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/select_info_to_edit.html'


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    # success_url = reverse_lazy('mylist:mylist')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        # save the user
        form.save()

        # get user data, authenticate, and login
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']
        user = authenticate(self.request, email=email, password=password)
        login(self.request, user)

        # mylist will redirect to login if the login didn't work
        # super(SignUp, self).form_valid(form)
        # return super().form_valid(form)
        return redirect(to='mylist:mylist')
