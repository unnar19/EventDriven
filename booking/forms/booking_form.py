from django.forms import ModelForm, widgets
from django import forms
from booking.models import Booking
import datetime

COUNTRIES = [('is','Iceland'),('ir','Iran'),('za','South Africa')]


class CreateBookingForm(ModelForm):
    class Meta:
        model = Booking
        exclude = ['id']#,'user_id','event_id']
        #labels = {
        #      'amount':""
        #      }
        widgets = {
            'amount': widgets.NumberInput(attrs={'class': 'hiddenfieldf','id': 'form-amount','value':'1'}),
            'subtotal': widgets.TextInput(attrs={'id': 'sub_form','class': 'form-control hiddenfieldf'}),
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'street_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_num': widgets.NumberInput(attrs={'class': 'form-control'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'},choices=COUNTRIES),
            'city': widgets.TextInput(attrs={'class': 'form-control'})
        }
