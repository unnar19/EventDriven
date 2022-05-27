from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/events
    path('', views.index, name='event-index'),
    path('<int:id>', views.get_event_by_id, name ='event_details')
]