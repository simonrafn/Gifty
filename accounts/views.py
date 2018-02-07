from django.urls import reverse_lazy
from django.views import generic
from customuser.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.


class SignUp(generic.CreateView):
    # form_class = UserCreationForm
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
        return redirect(to='mylist:mylist')
        # return super(SignUp, self).form_valid(form)
