# pages/urls.py
# pages/urls.py
from django.urls import path
from .views import ChatBotTemplateView, tahini_view

urlpatterns = [
    path('chat/', ChatBotTemplateView.as_view(), name='home'),
    path('', tahini_view, name='tahini'),
]
