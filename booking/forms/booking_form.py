from django.forms import ModelForm, widgets
from django import forms
from booking.models import Booking, Payment


class CreateBookingForm(ModelForm):
    hidden_del = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Booking
        exclude = ['id']
        # labels = {
        #     'email':"",
        #     'event_id':"",
        #     'amount':""
        #     }
        widgets = {
            'email': widgets.TextInput(attrs={'class': 'hiddenfield9','id': 'form-email'}),
            'event_id': widgets.NumberInput(attrs={'class': 'hiddenfield9','id': 'form-event_id'}),
            'amount': widgets.NumberInput(attrs={'class': 'hiddenfield9','id': 'form-amount','value':'1'}),
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
        fields = ('name_of_card_holder','card_number','exp_date','cvc')
        widgets = {
            'name_of_card_holder': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'exp_date': widgets.DateInput(attrs={'class': 'form-control'}),
            'cvc': widgets.NumberInput(attrs={'class': 'form-control'})
        }