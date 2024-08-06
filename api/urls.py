# api/urls.py
# api/urls.py

from django.urls import path
from .views import RasaChatBotView

urlpatterns = [
    path('chat/',RasaChatBotView.as_view(), name='rasa-chatbot'),
]
