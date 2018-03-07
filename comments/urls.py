from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('<int:item_pk>/', views.view_comments, name='view_comments'),
    path('<int:item_pk>/add/<int:visible_to_item_owner>/', views.add_comment, name='add_comment'),
]
