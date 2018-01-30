from django.db import models
from django.conf import settings


# Create your models here.
class Notification(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_seen = models.BooleanField(default=False)
    link = models.CharField(max_length=1000, null=True)
    message = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
