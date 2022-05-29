from django.shortcuts import render, get_object_or_404
from events.models import Event
from events.models import Ticket

# Create your views here.
def index(request):
    events = {'events': Event.objects.all().order_by('date')}
    return render(request, 'events/index.html', events)


def get_price_for_event(request, id):
    return render(request, 'events/index.html', {
        'ticket': get_object_or_404(Ticket, pk=id)
    })

def get_event_by_id(request, id):
    return render(request,'events/event_dietails.html', {
        'event': get_object_or_404(Event, pk=id)
    })


# def info_on_event_click(reqst)