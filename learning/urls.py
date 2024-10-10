from django.urls import path
from . import views

urlpatterns = [
    path('analyze-text/', views.analyze_text, name='analyze_text'),
    path('', views.index, name='index'),
    path('topic/<slug:slug>/', views.topic_detail, name='topic_detail'),
]

