from django.views.generic import ListView,DetailView
from .models import Event

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    paginate_by = 10  # Number of events to display per page

    def get_queryset(self):
        """Return the list of events."""
        return Event.objects.all().order_by('-date')  # Order by date, newest first

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'
