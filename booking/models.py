from django.db import models
from user.models import Account
from events.models import Event


class Booking(models.Model):
    email = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    event_id = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    address = models.CharField(max_length=150, blank=True, null=True)
    zip = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)


class Payment(models.Model):
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    subtotal = models.IntegerField()
    booking_id = models.ForeignKey(Booking, on_delete=models.SET_NULL, null=True)
    name_of_card_holder = models.CharField(max_length=250)
    card_number = models.IntegerField()
    exp_date = models.DateField()
    cvc = models.IntegerField()