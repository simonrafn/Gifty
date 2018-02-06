from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.base import ObjectDoesNotExist


# Create your models here.

class Comment(models.Model):
    item_id = models.ForeignKey('mylist.Item', on_delete=models.CASCADE)
    commenter_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)
    visible_to_owner = models.BooleanField()


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


class User(AbstractUser):
    email = models.EmailField(unique=True)
    # username = models.CharField(max_length=100)
    friends = models.ManyToManyField('self')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    # get a list of the friend requests that have been sent to you, and you haven't accepted/declined
    def get_friend_requests(self):
        return self.received_friend_requests.all()

    # send a friend request to a user,
    # add him if he has already sent you a friend request
    def send_friend_request(self, receiver):
        try:
            self.received_friend_requests.get(pk=receiver.pk)
            self.add_friend(receiver)
        except ObjectDoesNotExist:
            FriendRequest.objects.create(sender=self, receiver=receiver)
        """
        if self.received_friend_requests.filter(pk=receiver_id) is not None:
            self.add_friend(receiver_id)
        else:
            FriendRequest.objects.create(sender_id=self.pk, receiver_id=receiver_id)
        """

    # add a user to your friends list (you will also be added to their friends list),
    # and remove the friend request he sent you
    def add_friend(self, user_to_add):
        self.received_friend_requests.remove(sender=user_to_add, receiver=self)
        self.friends.add(user_to_add)

    # remove a user from your friends list (you will also be removed from their friends list)
    def remove_friend(self, user_to_remove):
        self.friends.remove(user_to_remove)
