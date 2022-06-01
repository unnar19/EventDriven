from django.forms import ModelForm, widgets
from django import forms
from booking.models import Booking, Payment


class CreateBookingForm(ModelForm):
    hidden_del = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Booking
        exclude = ['payment_id', 'id', 'ticket_id','event_id']
        widgets = {
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'amount': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'})
        }


class CreatePaymentForm(ModelForm):
    hidden_pay = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Payment
        exclude = ['id']
        fields = ('name_of_card_holder','card_number','exp_date','cvc')
        widgets = {
            'name_of_card_holder': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'exp_date': widgets.DateInput(attrs={'class': 'form-control'}),
            'cvc': widgets.TextInput(attrs={'class': 'form-control'})
        }