from django.http import HttpResponse
from django.shortcuts import render


def mylist(request):
    context = {}
    return render(request, 'mylist/mylist.html', context)

