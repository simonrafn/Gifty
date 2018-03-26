from django.urls import path
from . import views

app_name = 'contacts'
urlpatterns = [
    path('', views.get_contacts, name='contacts'),
    path('add/<int:user_pk>/', views.add_contact, name='add_contact'),
    path('remove/<int:user_pk>/', views.remove_contact, name='remove_contact'),
    path('accept/<int:user_pk>/', views.accept_friend_request_view, name='accept_friend_request_view'),
    path('decline/<int:user_pk>/', views.decline_friend_request_view, name='decline_friend_request_view'),
    path('count_friend_requests/', views.count_friend_requests, name='count_friend_requests'),
]
