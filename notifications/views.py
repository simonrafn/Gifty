from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notification


class ViewNotifications(LoginRequiredMixin, generic.ListView):
    model = Notification

    def get_queryset(self):
        return self.request.user.notifications.all().order_by('-date')
