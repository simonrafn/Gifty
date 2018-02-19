from django.test import TestCase
from customuser.models import User
from mylist.models import Item

import comments.models as comments


# Create your tests here.

class CommentTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='user1', email='u1@email.com', password='pass')
        item_owner = User.objects.get(username='user1')
        Item.objects.create(name='item1', price='1', owner=item_owner)

    def test_adding_comment(self):
        """It's possible to add a comment"""
        item = Item.objects.get(pk=1)
        commenter = User.objects.get(username='user1')
        comments.add_comment(item, commenter, message='message', visible_to_owner=False)
