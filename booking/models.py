from django.db import models
from user.models import Account
from events.models import Event
from django.contrib.auth.hashers import make_password


class Booking(models.Model):
    full_name = models.CharField(max_length=250, blank=True, null=True)
    user_id = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    event_id = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    amount = models.PositiveIntegerField()
    street_name = models.CharField(max_length=150, blank=True, null=True)
    house_num = models.PositiveIntegerField(blank=True, null=True)
    zip = models.PositiveIntegerField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)


class Payment(models.Model):
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    subtotal = models.IntegerField()
    booking_id = models.ForeignKey(Booking, on_delete=models.SET_NULL, null=True)
        