from django.db import models
from django.conf import settings
import logging
from django.db.models.base import ObjectDoesNotExist

logger = logging.getLogger(__name__)


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
    date = models.DateTimeField(auto_now_add=True)


# returns a queryset containing the users on the user friends list
def get_friends(user):
    return user.friends.all()


# returns a queryset containing the friend requests that have been sent to the user, and he hasn't accepted/declined
def get_friend_requests(user):
    return user.received_friend_requests.all()


# Sends a friend request to another user,
# or accepts his request if he's already sent you one,
# does not send a friend request if you've already sent one to that user,
# or if they are already friends
def send_friend_request(sender, receiver):
    are_friends = sender.friends.filter(pk=receiver.pk)
    receiver_already_sent_friend_request_to_sender = sender.received_friend_requests.filter(sender__pk=receiver.pk)
    sender_already_sent_friend_request_to_receiver = sender.sent_friend_requests.filter(receiver__pk=receiver.pk)

    if are_friends:
        return
    elif receiver_already_sent_friend_request_to_sender:
        accept_friend_request(sender, receiver)
    elif not sender_already_sent_friend_request_to_receiver:
        FriendRequest.objects.create(sender=sender, receiver=receiver)


# If accepted has sent acceptor a friend request, add accepted to acceptor friends list
# Also deletes the friend request
def accept_friend_request(acceptor, accepted):
    try:
        acceptor.received_friend_requests.get(sender__pk=accepted.pk).delete()
        acceptor.friends.add(accepted)
    except ObjectDoesNotExist:
        logger.exception("User attempted to accept a friend request that didn't exist")


# Delete a friend request sent from declined to decliner, if it exists
def decline_friend_request(decliner, declined):
    try:
        decliner.received_friend_requests.get(sender__pk=declined.pk).delete()
    except ObjectDoesNotExist:
        logger.exception("User attempted to decline a friend request that didn't exist")


# The users are removed from each others friends lists
def remove_friend(remover, removed):
    remover.friends.remove(removed)
