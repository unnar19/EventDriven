from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/events
    path('', views.index, name='event-index'),
]