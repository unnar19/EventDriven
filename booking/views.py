from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, get_list_or_404
from events.models import Event,Ticket
from booking.forms.booking_form import CreatePaymentForm, CreateBookingForm


def index(request):
    return render(request, 'booking/index.html')

@login_required
def book_an_event(request, id):
    return render(request, 'booking/booking_details.html', {
        'event': get_object_or_404(Event, pk=id),
        'price': get_list_or_404(Ticket, event_id=id)[0].price
    })


# def create_user(request):
#     if request.method == 'POST':
#         formpay = CreatePaymentForm(data=request.POST)
#         if formpay.is_valid():
#             user = formpay.save()
#             return redirect('booking-index')
#     else:
#         form = CreatePaymentForm()
#     return render(request, 'user/create_user.html',{
#         'form': form
#     })