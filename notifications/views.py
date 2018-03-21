from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from .models import Notification


class ViewNotifications(LoginRequiredMixin, generic.ListView):
    model = Notification

    def get_queryset(self):
        result = self.request.user.notifications.order_by('-date')
        # evaluate the queryset, so all the notifications can be set to seen, without modifying the results
        len(result)
        self.request.user.notifications.update(is_seen=True)
        return result


class CountUnseenNotifications(LoginRequiredMixin, generic.View):
    def get(self, request):
        return JsonResponse(
            {'number_of_unseen_notifications': request.user.notifications.filter(is_seen=False).count()}
        )
