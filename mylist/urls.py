from django.urls import path
from . import views

app_name = 'mylist'
urlpatterns = [
    path('', views.my_list, name='mylist'),
    path('add/', views.add_item, name='add_item'),
    path('edit/<int:item_pk>/', views.edit_item, name='edit_item'),
]
