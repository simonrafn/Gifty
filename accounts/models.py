from django.db import models
from customuser.models import User
from django.db.utils import IntegrityError

import logging

logger = logging.getLogger(__name__)


# Create your models here.

# NEEDs to be changed, probably doesn't work at all in its current state
def change_profile_image(user, image_path):  # not sure if this should be image path or something else
    user.profile_image = image_path
    user.save()


def is_username_available(username):
    return False if User.objects.filter(username=username).exists() else True


def change_username(user, new_username):
    try:
        User.objects.filter(pk=user.pk).update(username=new_username)
    except IntegrityError:
        logger.exception("An attempt was made to change a username to a username that was already taken.")


def is_email_available(email):
    return False if User.objects.filter(email=email).exists() else True


def change_email(user, new_email):
    try:
        User.objects.filter(pk=user.pk).update(email=new_email)
    except IntegrityError:
        logger.exception("An attempt was made to change an email to an email that was already taken.")
