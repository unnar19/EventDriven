from django.forms import ModelForm, widgets
from django import forms
from booking.models import Booking
import datetime
from django_countries.fields import CountryField




class CreateBookingForm(ModelForm):
    class Meta:
        model = Booking
        exclude = ['id','user_id','event_id']
        labels = {
              'amount':"",
              'subtotal':""
              }
        widgets = {
            'amount': widgets.NumberInput(attrs={'class': 'hiddenfield','id': 'form-amount','value':'1'}),
            'subtotal': widgets.TextInput(attrs={'id': 'sub_form','class': 'form-control hiddenfield'}),
            'full_name': widgets.TextInput(attrs={'id':'form_name', 'class': 'form-control',}),
            'street_name': widgets.TextInput(attrs={'id':'form_street','class': 'form-control',}),
            'house_num': widgets.NumberInput(attrs={'id':'form_num','class': 'form-control', }),
            'zip': widgets.NumberInput(attrs={'id':'form_zip','class': 'form-control'}),
            'country': widgets.Select(attrs={'id':'form_count','class': 'form-control'},),#choices=COUNTRIES.values()),
            'city': widgets.TextInput(attrs={'id':'form_city','class': 'form-control'}),
            
        }
