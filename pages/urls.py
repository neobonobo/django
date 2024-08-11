# pages/urls.py
# pages/urls.py
from django.urls import path
from .views import ChatBotTemplateView, tahini_view

urlpatterns = [
    path('', ChatBotTemplateView.as_view(), name='home'),
    path('tahini/', tahini_view, name='tahini'),
]
