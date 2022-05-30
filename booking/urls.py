from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/booking
    path('', views.index, name='booking-index'),
    path('<int:id>', views.book_an_event, name ='booking_details')
]