from django.db import models
from django.conf import settings
from mylist.models import Item
from django.db.models.base import ObjectDoesNotExist
from django.db import IntegrityError

import logging

logger = logging.getLogger(__name__)


# Create your models here.

class Comment(models.Model):
    item = models.ForeignKey(
        'mylist.Item',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    commenter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments_made'
    )
    message = models.CharField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)
    visible_to_owner = models.BooleanField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.message


# marks a comment as 'deleted'
def delete_comment(comment):
    Comment.objects.filter(pk=comment.pk).update(is_deleted=True)


# adds a comment to an items comment thread
# it's date is set as the current date
def add_comment(item, commenter, message, visible_to_owner):
    try:
        Comment.objects.create(
            item=item,
            commenter=commenter,
            message=message,
            visible_to_owner=visible_to_owner
        )
    except IntegrityError:
        logger.exception("There was an attempt to create a comment where either the item, or the commenter don't exist.")
