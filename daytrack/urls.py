# urls.py
from django.urls import path
from .views import dashboard_view, create_day_view, DayUpdateView 

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),  # User's dashboard
    path('dashboard/create-day/', create_day_view, name='create-day'),  # New URL for creating the day
    path('day/update/<int:pk>/', DayUpdateView.as_view(), name='day-update'),  # Update URL
]
