from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404

from .forms import ItemForm
from .models import Item
from .models import get_item_list

@login_required
def my_list(request):
    # form = ItemForm() # was used when the new item form was presented on the mylist page, currently it has its own page
    item_list = get_item_list(request.user)
    return render(request, 'mylist/mylist.html', {'item_list': item_list})


@login_required
def add_item(request):
    if request.method == 'GET':
        form = ItemForm()
        return render(request, 'mylist/add_item.html', {'form': form})
    elif request.method == 'POST':
        success_message = 'The item was created.'
        error_message = 'There was an error. The item was not created.'
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            messages.success(request, success_message)
        else:
            messages.error(request, error_message)

        return redirect(to='mylist:mylist')


@login_required
def edit_item(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    if request.method == 'GET':
        form = ItemForm(instance=item)
        return render(request, 'mylist/edit_item.html', {'form': form})
    elif request.method == 'POST':
        success_message = 'The item was changed.'
        error_message = 'There was an error. The item was not changed.'
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, success_message)
        else:
            messages.error(request, error_message)
        return redirect(to='mylist:mylist')




"""
def mylist(request):
    context = {}
    return render(request, 'mylist/mylist.html', context)
"""
