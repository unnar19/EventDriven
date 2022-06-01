from django.forms import ModelForm, widgets
from django import forms
from booking.models import Booking, Payment
import datetime



class CreateBookingForm(ModelForm):
    hidden_del = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Booking
        exclude = ['id','user_id','event_id']
        labels = {
             'amount':""
             }
        widgets = {
            'amount': widgets.NumberInput(attrs={'class': 'hiddenfield','id': 'form-amount','value':'1'}),
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'street_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_num': widgets.NumberInput(attrs={'class': 'form-control'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'})
        }


class CreatePaymentForm(ModelForm):
    hidden_pay = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Payment
        exclude = ['id']
        # fields = ('name_of_card_holder','card_number','exp_date','cvc')
        widgets = {
            'subtotal': widgets.TextInput(attrs={'class': 'form-control'}),

        }

class BookEventForm(ModelForm):
    class Meta:
        model = Booking
        exclude = ['id','user_id','event_id']
        labels = {
             'amount':""
             }
        widgets = {
            'amount': widgets.NumberInput(attrs={'class': 'hiddenfield','id': 'form-amount','value':'1'}),
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'street_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_num': widgets.NumberInput(attrs={'class': 'form-control'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'})
        }