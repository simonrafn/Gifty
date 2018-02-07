from django.db import models
from django.conf import settings


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=1000, null=True)
    price = models.CharField(max_length=20)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='items'
    )
    is_removed = models.BooleanField(default=False)
    reserver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
        related_name='reservations'
    )
