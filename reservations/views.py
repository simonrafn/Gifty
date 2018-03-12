from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from mylist.models import get_reservations


@login_required
def reservations(request):
    item_list = get_reservations(request.user)
    return render(request, 'reservations/reservations.html', {'item_list': item_list})
