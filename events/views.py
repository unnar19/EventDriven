from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from datetime import datetime
from events.models import Event

def index(request):
    today = datetime.today()
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        events = [ {
            'id': x.id,
            'image': x.image_url,
            'name': x.name,
            'start_date': x.start_date,
        }for x in Event.objects.filter(start_date__gte=today, name__icontains = search_filter).order_by('start_date')]
        return JsonResponse({'data': events})
    
    context = {'events': Event.objects.filter(start_date__gte=today).order_by('start_date')}
    # tickets = {'ticket': Ticket.objects.all()}
    return render(request, 'events/index.html', context)


def get_event_by_id(request, id):
    return render(request,'events/event_dietails.html', {
        'event': get_object_or_404(Event, pk=id)
    })

