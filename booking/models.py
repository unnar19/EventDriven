from django.db import models
from user.models import Account
from events.models import Ticket

class Payment(models.Model):
    time = models.TimeField()
    date = models.DateField()
    subtotal = models.IntegerField()
    masked_card_num = models.CharField(max_length=200)
    retrieval_ref_num = models.CharField(max_length=200)

class Booking(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    amount = models.IntegerField()
    address = models.CharField(max_length=150)
    zip = models.IntegerField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)