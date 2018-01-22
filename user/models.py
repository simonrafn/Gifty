from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=200, unique=True)
    avatar = models.CharField(max_length=10) # Temporary, replace later with something that can store images


class Comment(models.Model):
    item_id = models.ForeignKey('mylist.Item', on_delete=models.CASCADE)
    commenter_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    message = models.CharField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)
    visible_to_owner = models.BooleanField()

