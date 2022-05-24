from django.db import models


class Categories(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)

class Event(models.Model):
    event_id = models.IntegerField(primary_key=True)
    image_url = models.CharField(max_length=9999)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    time = models.TimeField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    max_attendees = models.IntegerField()

class Account(models.Model):
    acc_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    image_url = models.CharField(max_length=9999)

class Ticket(models.Model):
    ticket_id = models.IntegerField(primary_key=True)
    price = models.IntegerField()
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)

class Favourite(models.Model):
    fav_id = models.IntegerField(primary_key=True)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    acc_id = models.ForeignKey(Account, on_delete=models.CASCADE)

class Payment(models.Model):
    payment_id = models.IntegerField(primary_key=True)
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

