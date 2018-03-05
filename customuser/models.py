from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    # username = models.CharField(max_length=100)
    friends = models.ManyToManyField('self')

    profile_image = None  # should be some kind of image field

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


"""
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
"""

"""
# get a queryset of the users on your friends list
def get_friends(self):
    return self.friends.all()

# get a queryset of the friend requests that have been sent to you, and you haven't accepted/declined
def get_friend_requests(self):
    return self.received_friend_requests.all()

# create a friend request directed at a user,
# add him if he has already sent you a friend request
def send_friend_request(self, receiver):
    try:
        self.received_friend_requests.get(sender__pk=receiver.pk)
        self.accept_friend_request(receiver)
    except ObjectDoesNotExist:
        FriendRequest.objects.create(sender=self, receiver=receiver)

# Add a user to your friends list, given that they've sent you a friend request
# Also deletes the friend request
def accept_friend_request(self, sender):
    try:
        self.received_friend_requests.get(sender__pk=sender.pk).delete()
        self.friends.add(sender)
    except ObjectDoesNotExist:
        logging.exception("User attempted to accept a friend request that didn't exist")

# remove a user from your friends list (you will also be removed from their friends list)
def remove_friend(self, user_to_remove):
    self.friends.remove(user_to_remove)
"""