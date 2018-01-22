from django.db import models


# Create your models here.

class Contacts(models.Model):
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    contact_id = models.ForeignKey('user.User', on_delete=models.CASCADE)


class FriendRequest(models.Model):
    requester_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    contact_id = models.ForeignKey('user.User', on_delete=models.CASCADE)

