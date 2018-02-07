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
    link = models.CharField(max_length=1000, null=True)
    message = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def set_as_seen(self):
        self.is_seen = True


# get all notifications directed at a user, that he hasn't seen
def get_unseen_notifications(user):
    return user.notifications.filter(is_seen=False)


# get all notifications directed at a user
def get_notifications(user):
    return user.notifications.all()


# create a notification directed at a user
# it is marked as unseen, and the date is marked as the current date
def create_notification(user, link, message):
    Notification.objects.create(user=user, link=link, message=message)


# deletes the notification
def delete_notification(notification):
    notification.detele()


# sets the notification as seen by the user that it's directed at
def set_notification_as_seen(notification):
    notification.is_seen = True
