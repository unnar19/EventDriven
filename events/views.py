from django.shortcuts import render
from events.models import Event

# Create your views here.
def index(request):
    events = {'events': Event.objects.all().order_by('name')}
    return render(request, 'events/index.html', events)