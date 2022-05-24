from django.shortcuts import render

event = [
    {'name': 'MLM', 'price': 69.99 },
    {'name': 'HERBS LIFE', 'price': 96.66 }
]

# Create your views here.
def index(request):
    return render(request, 'events/index.html', context={'event': event })
