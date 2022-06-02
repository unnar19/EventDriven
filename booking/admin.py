from django.contrib import admin
from events.models import Event, Categories
from booking.models import Booking
from user.models import Account

# Register your models here.
admin.site.register(Event)
admin.site.register(Categories)
admin.site.register(Booking)
admin.site.register(Account)
