from django.contrib.auth.models import AbstractUser
from django.db import models
from events.models import Categories


class Account(AbstractUser):
    fav_cat = models.ForeignKey(Categories, on_delete=models.SET_NULL, blank=True , null=True)
    image = models.ImageField(upload_to='profile-pics', blank= True, null=True)
    image_url = models.CharField(max_length=9999, null= True)