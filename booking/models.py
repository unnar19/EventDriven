import email
from operator import truediv
from django.db import models
from user.models import Account
from events.models import Event
from django_countries.fields import CountryField


class Booking(models.Model):
    full_name = models.CharField(max_length=250)
    user_id = models.ForeignKey(Account, on_delete=models.SET_NULL, blank=True, null=True)
    event_id = models.ForeignKey(Event, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.PositiveIntegerField()
    email_delivery = models.BooleanField(default=False)
    street_name = models.CharField(max_length=150)
    house_num = models.PositiveIntegerField()
    zip = models.PositiveIntegerField()
    country = CountryField(blank=True, null=True)
    city = models.CharField(max_length=100)
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    subtotal = models.IntegerField()
        