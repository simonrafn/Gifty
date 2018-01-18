from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('index/index.html')

    context = {

    }

    return HttpResponse(template.render(context, request))

    #return HttpResponse("<h1>Welcome to the soon to be login page :)</h1>")
#    return render(request, 'blog/post_list.html')

