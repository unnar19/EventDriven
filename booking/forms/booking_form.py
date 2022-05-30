from django.forms import ModelForm, widgets
from django import forms
from booking.models import Booking, Payment


class CreatePaymentForm(ModelForm):

    class Meta:
        model = Payment
        exclude = ['id']
        fields = ('date',)
        widgets = {
            #'time': widgets.TextInput(attrs={'class': 'form-control'}),
            'date': widgets.TextInput(attrs={'class': 'form-control'}),
            'subtotal': widgets.TextInput(attrs={'class': 'form-control'}),
            'masked_card_num': widgets.TextInput(attrs={'class': 'form-control'}),
            'retrieval_ref_num': widgets.TextInput(attrs={'class': 'form-control'})
        }

class CreateBookingForm(ModelForm):
    class Meta:
        model = Booking
        exclude = ['payment_id', 'id', 'ticket_id']
        widgets = {
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'amount': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'})
        }
