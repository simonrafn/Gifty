from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from .models import Notification


class ViewNotifications(LoginRequiredMixin, generic.ListView):
    model = Notification

    def get_queryset(self):
        page_number = self.kwargs['page_number']
        results_per_page = 10
        result = self.request.user.notifications.order_by('-date')[(page_number-1)*results_per_page:page_number*results_per_page]
        # evaluate the queryset, so all the notifications can be set to seen, without modifying the results returned to the template
        len(result)
        self.request.user.notifications.filter(id__in=result).update(is_seen=True)
        return result


class CountUnseenNotifications(LoginRequiredMixin, generic.View):
    def get(self, request):
        return JsonResponse(
            {'number_of_unseen_notifications': request.user.notifications.filter(is_seen=False).count()}
        )
