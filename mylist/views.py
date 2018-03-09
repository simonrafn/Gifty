from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404

from .forms import ItemForm
from .models import Item
from .models import get_item_list
from .models import remove_item_from_list
from customuser.models import User
from contacts.models import are_friends


@login_required
def index(request):
    username = request.user.username
    return redirect(to='/list/'+username)


@login_required
def my_list(request, username):
    if request.user.username is username:
        item_list = get_item_list(request.user)
        return render(request, 'mylist/mylist.html', {'item_list': item_list})
    else:
        contact = get_object_or_404(User, username__iexact=username)
        if are_friends(request.user, contact):
            item_list = get_item_list(contact)
            return render(request, 'mylist/otherlist.html', {'item_list': item_list,
                                                             'are_friends': are_friends(request.user, contact),
                                                             'contact': contact, })
        else:
            has_received = request.user.received_friend_requests.filter(sender__pk=contact.pk)
            has_sent = request.user.sent_friend_requests.filter(receiver__pk=contact.pk)
            return render(request, 'mylist/otherlist.html', {'are_friends': are_friends(request.user, contact),
                                                             'contact': contact,
                                                             'has_received': has_received,
                                                             'has_sent': has_sent, })




@login_required
def add_item(request, username):
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

        return redirect(to='mylist:mylist', username=username)


@login_required
def edit_item(request, username, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    if item.owner == request.user:
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
    else:
        error_message = "There was an error. You cannot edit that item."
        messages.error(request, error_message)
        return redirect(to='mylist:mylist')


@login_required
def delete_item(request, username, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    if item.owner == request.user:
        success_message = 'The item was deleted.'
        messages.success(request, success_message)
        remove_item_from_list(item)
    else:
        error_message = 'There was an error. You cannot delete that item.'
        messages.error(request, error_message)
    return redirect(to='mylist:mylist')
