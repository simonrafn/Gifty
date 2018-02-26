from django.db import models
from django.conf import settings


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=1000, blank=True)
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

    def __str__(self):
        return self.name


# get all items from a users item list, which he hasn't 'removed'
def get_item_list(user):
    return user.items.filter(is_removed=False).order_by('-pk')


# mark an item as removed from a users list
def remove_item_from_list(item):
    # user.items.remove(item)
    item.is_removed = True
    item.save(update_fields=['is_removed'])


# get an item by its id/pk
# returns None if the item doesn't exist
def get_item(item_id):
    item_results = Item.objects.filter(pk=item_id)
    return item_results.get(pk=item_id) if item_results else None


# mark an item as reserved by the user
def reserve_item(user, item):
    item.reserver = user
    item.save(update_fields=['reserver'])


# mark an item as not being reserved anymore
def unreserve_item(item):
    item.reserver = None
    item.save(update_fields=['reserver'])
