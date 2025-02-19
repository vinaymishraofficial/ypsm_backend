from django.shortcuts import render
from .models import Event

# Create your views here.

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    context = {
        'event': event,
    }
    return render(request, 'events/event_detail.html', context)
