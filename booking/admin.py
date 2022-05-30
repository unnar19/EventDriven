from django.contrib import admin
from events.models import Event, Categories, Ticket

# Register your models here.
admin.site.register(Event)
admin.site.register(Categories)
admin.site.register(Ticket)
