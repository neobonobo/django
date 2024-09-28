# urls.py
from django.urls import path
from .views import dashboard_view,  DayUpdateView ,logout_view

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),  # User's dashboard
    path('day/update/<int:pk>/', DayUpdateView.as_view(), name='day-update'),  # Update URL
    path('logout/', logout_view, name='logout'),
]
