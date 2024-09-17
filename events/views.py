from django.views.generic import ListView,DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Event, Attendee
from .forms import AttendeeForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AttendeeForm()
        return context

    def post(self, request, *args, **kwargs):
        form = AttendeeForm(request.POST)
        event = self.get_object()

        if form.is_valid():
            attendee = form.save(commit=False)
            attendee.event = event
            attendee.save()
            return redirect('event-detail', pk=event.pk)

        return render(request, 'events/event_detail.html', {'event': event, 'form': form})
