from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from userprofile.forms import CustomUserForm
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


def home(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect(to='mylist:mylist')
            # return HttpResponse("User was created successfully.")
        else:
            return HttpResponse("There was an error.")
    else:
        form = CustomUserForm()
    return render(request, 'accounts/signup.html', {'form': form})
