from django.urls import path
from .views import rasa_webhook,conversation_history,chat_view

urlpatterns = [
    path('rasa/', rasa_webhook, name='rasa_webhook'),
    path('history/', conversation_history, name='conversation_history'),
    path('chat/', chat_view, name='chat_view'),
]
