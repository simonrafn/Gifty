from django.db import models
from django.conf import settings


# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    is_seen = models.BooleanField(default=False)
    link = models.CharField(max_length=1000, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=1000)

    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='+'
    )

    def __str__(self):
        return self.message

    def set_as_seen(self):
        self.is_seen = True
        self.save(update_fields=['is_seen'])


# get all notifications directed at a user, that he hasn't seen
def get_unseen_notifications(user):
    return user.notifications.filter(is_seen=False)
