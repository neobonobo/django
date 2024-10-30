from django.urls import path
from . import views

urlpatterns = [
    path('analyze-text/', views.analyze_text, name='analyze_text'),
    path('', views.interests, name='interests'),
    path('topic/<slug:slug>/', views.topic_detail, name='topic_detail'),
    path('chatbot/', views.chatbot_view, name='chatbot'),
    path('ai/', views.ai_view, name='ai'),
]

