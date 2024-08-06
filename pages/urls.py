# pages/urls.py
# pages/urls.py
from django.urls import path
from .views import ChatBotTemplateView

urlpatterns = [
    path('', ChatBotTemplateView.as_view(), name='home'),
]
