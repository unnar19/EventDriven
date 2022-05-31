from django.contrib import admin
from events.models import Event, Categories, Ticket
from booking.models import Booking, Payment
from user.models import Account

# Register your models here.
admin.site.register(Event)
admin.site.register(Categories)
admin.site.register(Ticket)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Account)
