# urls.py
from django.urls import path
from .views import dashboard_view, create_day_view, DayUpdateView 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),  # User's dashboard
    path('dashboard/create-day/', create_day_view, name='create-day'),  # New URL for creating the day
    path('day/update/<int:pk>/', DayUpdateView.as_view(), name='day-update'),  # Update URL
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
