from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, get_list_or_404
from events.models import Event,Ticket

def index(request):
    return render(request, 'booking/index.html')

def book_an_event(request, id):
    return render(request, 'booking/booking_details.html', {
        'event': get_object_or_404(Event, pk=id),
        'price': get_list_or_404(Ticket, event_id=id)[0].price
    })