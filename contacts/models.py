from django.db import models
from django.conf import settings
import logging
from django.db.models.base import ObjectDoesNotExist

# Create your models here.


class FriendRequest(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sent_friend_requests'
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='received_friend_requests'
    )


# returns a queryset containing the users on the user friends list
def get_friends(user):
    return user.friends.all()


# returns a queryset containing the friend requests that have been sent to the user, and he hasn't accepted/declined
def get_friend_requests(user):
    return user.received_friend_requests.all()


# create a friend request directed at receiver,
# add receiver to sender's friends list if receiver has already sent sender a friend request
def send_friend_request(sender, receiver):
    try:
        sender.received_friend_requests.get(sender__pk=receiver.pk)
        accept_friend_request(sender, receiver)
    except ObjectDoesNotExist:
        FriendRequest.object.create(sender=sender, receiver=receiver)


# If accepted has sent acceptor a friend request, add accepted to acceptor friends list
# Also deletes the friend request
def accept_friend_request(acceptor, accepted):
    try:
        acceptor.received_friend_requests.get(sender__pk=accepted.pk).delete()
        acceptor.friends.add(accepted)
    except ObjectDoesNotExist:
        logging.exception("User attempted to accept a friend request that didn't exist")


# Remove a friend request sent from declined to decliner, if it exists
def decline_friend_request(decliner, declined):
    try:
        decliner.received_friend_requests.get(sender__pk=declined.pk).remove()
    except ObjectDoesNotExist:
        logging.exception("User attempted to decline a friend request that didn't exist")


# remove removed from remover friends list (remover will also be removed from removed friends list)
def remove_friend(remover, removed):
    remover.friends.remove(removed)
