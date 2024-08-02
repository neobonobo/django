# api/urls.py

from django.urls import path
from .views import ChatView, rasa_webhook

urlpatterns = [
    path('chat/', ChatView.as_view(), name='chat'),
    path('rasa-webhook/', rasa_webhook, name='rasa_webhook'),
]
