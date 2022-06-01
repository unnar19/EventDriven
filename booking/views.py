from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from events.models import Event
from booking.forms.booking_form import CreatePaymentForm, CreateBookingForm


def index(request):
    return render(request, 'booking/index.html')

#
# def book_an_event(request, id):
#     return render(request, 'booking/booking_details.html', {
#         'event': get_object_or_404(Event, pk=id),
#         'price': get_list_or_404(Ticket, event_id=id)[0].price
#     })

# formpay = CreatePaymentForm(data=request.POST)
#         if formpay.is_valid():
#             user = formpay.save()
#             return redirect('booking-index')

@login_required
def book_an_event(request, id):
    formdel = CreateBookingForm()
    formpay = CreatePaymentForm()
    if request.method == 'POST':
        if 'hidden_del' in request.POST:
            formdel = CreateBookingForm(data=request.POST)
            if formdel.is_valid():
                formdel.save()
                return redirect('booking-index')
        if 'hidden_pay' in request.POST:
            formpay = CreatePaymentForm(data=request.POST)
            if formpay.is_valid():
                formpay.save()
                return redirect('booking-index')
        
    return render(request, 'booking/booking_details.html', {
        'formdel': formdel,
        'formpay': formpay,
        'event': get_object_or_404(Event, pk=id)
    })