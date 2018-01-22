from django.db import models


# Create your models here.

class Contacts(models.Model):
    user_id = models.ForeignKey('index.User')
    contact_id = models.ForeignKey('index.User')


class FriendRequest(models.Model):
    requester_id = models.ForeignKey('index.User')
    contact_id = models.ForeignKey('index.User')

