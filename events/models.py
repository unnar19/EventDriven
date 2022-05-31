from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Event(models.Model):
    image_url = models.CharField(max_length=9999)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    time = models.TimeField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=100)
    max_attendees = models.IntegerField()


class Ticket(models.Model):
    price = models.IntegerField()
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)







