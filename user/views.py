from django.shortcuts import render
from user.models import Account


# Create your views here.
def index(request):
    return render(request, 'user/index.html',{
        'user': Account.objects.all()
    })
