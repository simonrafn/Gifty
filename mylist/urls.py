from django.urls import path
from . import views

app_name = 'mylist'
urlpatterns = [
    path('', views.mylist, name='mylist'),
]
