from user.forms.user_form import UserCreateForm
from django.shortcuts import render, get_object_or_404, redirect
from user.models import Account

# Create your views here.
def index(request):
    return render(request, 'user/index.html',{
        'user': Account.objects.all()
    })

def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user-index')
    else:
        form = UserCreateForm()
    return render(request, 'user/create_user.html',{
        'form': form
    })