from django.db import models
from django.conf import settings


# Create your models here.

class Comment(models.Model):
    item = models.ForeignKey('mylist.Item', on_delete=models.CASCADE)
    commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)
    visible_to_owner = models.BooleanField()
    is_deleted = models.BooleanField(default=False)


# marks a comment as 'deleted'
def delete_comment(comment):
    comment.is_deleted = True


# adds a comment to an items comment thread
# it's date is set as the current date
def add_comment(item, commenter, message, visible_to_owner):
    item.
