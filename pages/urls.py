from django.urls import path
from .views import TahiniPageView

urlpatterns = [
    path('tahini/', TahiniPageView.as_view(), name='tahini_page'),
]
