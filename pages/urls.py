# pages/urls.py
# pages/urls.py
from django.urls import path
from .views import ChatBotTemplateView, tahini_view, cv_view, HomePageView

urlpatterns = [
    path('chat/', ChatBotTemplateView.as_view(), name='chat'),
    path('tahini', tahini_view, name='tahini'),
    path('',HomePageView.as_view(), name='home'),
    path('cv/', cv_view, name='cv'),
]
