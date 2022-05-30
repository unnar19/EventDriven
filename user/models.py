from django.contrib.auth.models import AbstractUser
from django.db import models
from events.models import Categories


class Account(AbstractUser):
    fav_cat = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    image_url = models.CharField(max_length=9999)


class Favourite(models.Model):
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    acc_id = models.ForeignKey(Account, on_delete=models.CASCADE)