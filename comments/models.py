from django.db import models
from django.conf import settings


# Create your models here.

class Comment(models.Model):
    item_id = models.ForeignKey('mylist.Item', on_delete=models.CASCADE)
    commenter_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)
    visible_to_owner = models.BooleanField()
