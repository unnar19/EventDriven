from django.db import models
from events.models import Categories

class Account(models.Model):
    acc_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    image_url = models.CharField(max_length=9999)

class Favourite(models.Model):
    fav_id = models.IntegerField(primary_key=True)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    acc_id = models.ForeignKey(Account, on_delete=models.CASCADE)
