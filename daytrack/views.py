# daytrack/views.py
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import Day
from events.models import Event
from .forms import DayForm

def dashboard_view(request):
    today = timezone.now().date()
    user = request.user

    # Check if the Day object for today exists
    day = Day.objects.filter(user=user, wake_up_time__date=today).first()
    events = Event.objects.filter(end_date__gte=today)
    if not day:
        # If there is no day object for today, show the "I'm Up" button
        return render(request, 'daytrack/dashboard.html', {'created': True})  # created=True indicates to show the button

    # If the day object exists, show its details
    return render(request, 'daytrack/dashboard.html', {'day': day, 'events': events,'created': False})
def create_day_view(request):
    if request.method == "POST":
        today = timezone.now().date()
        # Ensure no duplicate entries are created
        day, created = Day.objects.get_or_create(user=request.user, date=today)
        day.wake_up_time = timezone.now()  # Set wake-up time when the button is clicked
        day.save()
        return redirect('dashboard')
    return redirect('dashboard')
class DayUpdateView(UpdateView):
    model = Day
    form_class = DayForm
    template_name = 'daytrack/update_day.html'
    
    def get_object(self, queryset=None):
        today = timezone.now().date()
        return get_object_or_404(Day, user=self.request.user, wake_up_time__date=today)

    def get_success_url(self):
        return reverse_lazy('dashboard')  # Redirect to the dashboard after updating
def logout_view(request):
    logout(request)
