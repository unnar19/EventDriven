from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from events.models import Event
from booking.models import Booking
from user.models import Account
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
    event = get_object_or_404(Event, pk=id)
    current_user = get_object_or_404(Account, pk=request.user.id)
    formdel = CreateBookingForm()
    formpay = CreatePaymentForm()
    if request.method == 'POST':
        if 'hidden_del' in request.POST:
            formdel = CreateBookingForm(data=request.POST)
            if formdel.is_valid():
                del_dict = formdel.cleaned_data
                del_model = Booking(
                    full_name = del_dict["full_name"],
                    user_id = current_user,
                    event_id = event,
                    amount = del_dict["amount"],
                    street_name = del_dict["street_name"],
                    house_num = del_dict["house_num"],
                    zip = del_dict["zip"],
                    country = del_dict["country"],
                    city = del_dict["city"]
                )
                del_model.save()

                # return redirect('booking-index')
        if 'hidden_pay' in request.POST:
            formpay = CreatePaymentForm(data=request.POST)
            if formpay.is_valid():
                formpay.save()
                # return redirect('booking-index')
        
    return render(request, 'booking/booking_details.html', {
        'formdel': formdel,
        'formpay': formpay,
        'event': event
    })