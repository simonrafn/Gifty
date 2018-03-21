from django.urls import path

from . import views

app_name = 'notifications'
urlpatterns = [
    path('', views.ViewNotifications.as_view(), name='view_notifications'),
    path('count_unseen_notifications/', views.CountUnseenNotifications.as_view(), name='count_unseen_notifications'),

]