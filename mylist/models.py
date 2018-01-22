from django.db import models
from user import models as user_models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=1000, null=True)
    price = models.CharField(max_length=20)
    owner_id = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    is_removed = models.BooleanField(default=False)
    reserver_id = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE)

