from django.urls import reverse

from .models import Notification


def friend_request_accepted_notification(request_sender, request_receiver):
    message = request_receiver.username + " has accepted your friend request."
    link = reverse('mylist:mylist', kwargs={'username': request_receiver.username})
    Notification.objects.create(
        user=request_sender,
        link=link,
        actor=request_receiver,
        message=message
    )
