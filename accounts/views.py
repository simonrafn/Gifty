from django.urls import reverse_lazy
from django.views import generic
from userprofile.forms import CustomUserCreationForm
from userprofile.models import User
from django.contrib.auth import authenticate, login

# Create your views here.


class SignUp(generic.CreateView):
    # form_class = UserCreationForm
    form_class = CustomUserCreationForm
    # success_url = reverse_lazy('login')
    success_url = reverse_lazy('mylist:mylist')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        login(self.request, form.user)
        return super(SignUp, self).form_valid(form)

    """
        def form_valid(self, form):
        # save the new user first
        form.save()
        # get the username and password
        username = self.request.POST['email']
        password = self.request.POST['password1']
        # username = form.cleaned_data['email']
        # password = form.cleaned_data['password1']
        # authenticate user then login
        user = authenticate(email=username, password=password)
        login(self.request, user)
        return super(SignUp, self).form_valid(form)
    """
