from django.db import models


class Categories(models.Model):
    category_id = models.IntegerField()
    name = models.CharField(max_length=30)

class Event(models.Model):
    event_id = models.IntegerField()
    image_url = models.CharField(max_length=9999)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    category_id = models.IntegerField()
    time = models.TimeField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    max_attendees = models.IntegerField()

class Account(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    image_url = models.CharField(max_length=9999)

class Ticket(models.Model):
    ticket_id = models.IntegerField()
    price = models.IntegerField()
    event_id = models.IntegerField()

class Favourite(models.Model):
    fav_id = models.IntegerField()
    category_id = models.IntegerField()
    email = models.CharField(max_length=100)

class Payment(models.Model):
    time = models.TimeField()
    date = models.DateField()
    payment_id = models.IntegerField()
    subtotal = models.IntegerField()
    masked_card_num = models.CharField(max_length=200)
    retrieval_ref_num = models.CharField(max_length=200)

class Booking(models.Model):
    email = models.CharField(max_length=100)
    ticket_id = models.IntegerField()
    amount = models.IntegerField()
    address = models.CharField(max_length=150)
    zip = models.IntegerField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    payment_id = models.IntegerField()

