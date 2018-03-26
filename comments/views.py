from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from mylist.models import Item
from .models import Comment
from .forms import CommentForm


@login_required
def view_comments(request, username, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    if request.user == item.owner or request.user in item.owner.friends.all():
        context = {
            'form': CommentForm(),
            'item': item,
            'comments_visible_to_item_owner': item.comments.filter(visible_to_owner=True),
            'comments_not_visible_to_item_owner': item.comments.filter(visible_to_owner=False),
        }
        return render(request, 'comments/view_comments.html', context)
    else:
        error_message = 'You do not have access to that item.'
        messages.error(request, error_message)
        return render(request, 'error.html')


@login_required
def add_comment(request, username, item_pk, visible_to_item_owner):
    item = get_object_or_404(Item, pk=item_pk)
    if request.user == item.owner or request.user in item.owner.friends.all():
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.item = item
            comment.commenter = request.user
            print(visible_to_item_owner)
            comment.visible_to_owner = visible_to_item_owner
            comment.save()
        else:
            error_message = "There was an error. The comment was not created."
            messages.error(request, error_message)
        return redirect(to='mylist:view_comments', item_pk=item_pk, username=username)
    else:
        error_message = 'You do not have access to that item.'
        messages.error(request, error_message)
        return render(request, 'error.html')

