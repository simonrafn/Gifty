from django.db import models
from index import models as index_models


# Create your models here.
class Notification(models.Model):
    user_id = models.ForeignKey(index_models.User)
    is_seen = models.BooleanField(default=False)
    link = models.CharField(max_length=1000, null=True)
    message = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
