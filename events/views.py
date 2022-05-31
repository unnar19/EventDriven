from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from events.models import Event,Ticket
from datetime import datetime

def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        events = [ {
            'id': x.id,
            'image': x.image_url,
            'name': x.name,
            'start_date': x.start_date,
        }for x in Event.objects.filter(name__icontains = search_filter)]
        return JsonResponse({'data': events})

    today = datetime.today()
    context = {'events': Event.objects.filter(start_date__gte=today).order_by('start_date')}
    # tickets = {'ticket': Ticket.objects.all()}
    return render(request, 'events/index.html', context)


def get_event_by_id(request, id):
    return render(request,'events/event_dietails.html', {
        'event': get_object_or_404(Event, pk=id),
        'price': get_list_or_404(Ticket, event_id=id)[0].price
    })

