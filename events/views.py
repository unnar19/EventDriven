from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from events.models import Event,Ticket

# Create your views here.
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        events = [ {
            'id': x.id,
            'image': x.image_url,
            'name': x.name,
            'date': x.date
        }for x in Event.objects.filter(name__icontains = search_filter)]
        return JsonResponse({'data:': events})

    context = {'events': Event.objects.all().order_by('name')}
    # tickets = {'ticket': Ticket.objects.all()}
    return render(request, 'events/index.html', context)

def get_event_by_id(request, id):
    return render(request,'events/event_dietails.html', {
        'event': get_object_or_404(Event, pk=id)
    })