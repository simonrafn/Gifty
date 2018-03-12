from django.urls import path

from . import views
from comments import views as comments_views

app_name = 'mylist'
urlpatterns = [
    path('', views.my_list, name='own_list'),
    path('<username>/', views.my_list, name='mylist'),
    path('<username>/add/', views.add_item, name='add_item'),
    path('<username>/item=<int:item_pk>/edit/', views.edit_item, name='edit_item'),
    path('<username>/item=<int:item_pk>/delete/', views.delete_item, name='delete_item'),

    path('<username>/item=<int:item_pk>/comments/', comments_views.view_comments, name='view_comments'),
    path('<username>/item=<int:item_pk>/comments/add/<int:visible_to_item_owner>/',
         comments_views.add_comment, name='add_comment'),

    # path('<username>/item=<int:item_pk>/reserve/', views.reserve_item, name='reserve_item'),
    # path('<username>/item=<int:item_pk>/comments/', views.view_comments, name='view_comments'),

    # path('', views.index, name='index'),
]