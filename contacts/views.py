from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404

from .models import get_friends
from .models import get_friend_requests
from .models import send_friend_request
from .models import remove_friend
from .models import decline_friend_request
from .models import accept_friend_request

from customuser.models import User
from notifications.notifiers import friend_request_accepted_notification


@login_required
def get_contacts(request):
    contacts = get_friends(request.user)
    friend_requests = get_friend_requests(request.user)
    # TODO: klára contacts.html
    return render(request, 'contacts/contacts.html', {'contacts': contacts,
                                                      'friend_requests': friend_requests, })


@login_required
def add_contact(request, user_pk):
    receiver = get_object_or_404(User, pk=user_pk)
    send_friend_request(request.user, receiver)
    msg = 'Sent friend request to: ' + receiver.username
    messages.success(request, msg)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def remove_contact(request, user_pk):
    removed_friend = get_object_or_404(User, pk=user_pk)
    remove_friend(request.user, removed_friend)
    msg = 'Removed contact: ' + removed_friend.username
    messages.success(request, msg)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def accept_friend_request_view(request, user_pk):
    contact = get_object_or_404(User, pk=user_pk)
    accept_friend_request(request.user, contact)
    msg = 'Accepted the friend request from: ' + contact.username
    messages.success(request, msg)

    # create a notification for the event
    friend_request_accepted_notification(request_sender=contact, request_receiver=request.user)

    return redirect(to='contacts:contacts')


@login_required
def decline_friend_request_view(request, user_pk):
    contact = get_object_or_404(User, pk=user_pk)
    decline_friend_request(request.user, contact)
    msg = 'Declined the friend request from: ' + contact.username
    messages.success(request, msg)
    return redirect(to='contacts:contacts')
