from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/user
    path('', views.index, name='user-index'),
    path('create_user', views.create_user, name='create_user')
]