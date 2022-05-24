from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/booking
    path('', views.index, name='booking-index'),
]