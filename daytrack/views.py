from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import Day
from events.models import Event
from .forms import DayForm
from django.utils.timezone import localtime

def dashboard_view(request):
    # Get today's date based on the user's local time zone
    today = localtime(timezone.now()).date()
    user = request.user

    # Check if the Day object for today exists
    day = Day.objects.filter(user=user, wake_up_time__date=today).first()
    events = Event.objects.filter(end_date__gte=today)

    if not day:
        # If no day object exists for today, create a new Day object
        day = Day.objects.create(user=user, wake_up_time=timezone.now())

    # Render the dashboard with the day's details
    return render(request, 'daytrack/dashboard.html', {'day': day, 'events': events})
class DayUpdateView(UpdateView):
    model = Day
    form_class = DayForm
    template_name = 'daytrack/update_day.html'

    def get_object(self, queryset=None):
        # Ensure we get today's day object for the user
        today = localtime(timezone.now()).date()
        return get_object_or_404(Day, user=self.request.user, wake_up_time__date=today)

    def form_valid(self, form):
        # Save the form and redirect to the dashboard
        form.instance.user = self.request.user  # Ensure the correct user is set
        form.save()  # Save the form to update the Day object
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the dashboard after updating
        return reverse_lazy('dashboard')
def logout_view(request):
    logout(request)
    return redirect('login')
