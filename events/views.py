from django.shortcuts import render, get_object_or_404
from events.models import Event

# Create your views here.
def index(request):
    events = {'events': Event.objects.all().order_by('date')}
    return render(request, 'events/index.html', events)

def get_event_by_id(request, id):
    return render(request,'events/event_dietails.html', {
        'event': get_object_or_404(Event, pk=id)
    })