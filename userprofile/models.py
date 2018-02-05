from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Comment(models.Model):
    item_id = models.ForeignKey('mylist.Item', on_delete=models.CASCADE)
    commenter_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)
    visible_to_owner = models.BooleanField()


class FriendRequest(models.Model):
    requester_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sent_friend_requests'
    )
    contact_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='received_friend_requests'
    )


class User(AbstractUser):
    email = models.EmailField(unique=True)
    # username = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email



"""
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField('self')
    avatar = models.ImageField()  # have to add where to save images, should probably be set to MEDIA_URL ?
"""

