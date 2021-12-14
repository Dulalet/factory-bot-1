from django.urls import path

from user_messages.views import send_message, get_messages_by_user

urlpatterns = [
    path('send/', send_message, name='send_message'),
    path('getMessages/', get_messages_by_user, name='get_messages_by_user'),
]
