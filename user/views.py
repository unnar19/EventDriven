from user.forms.user_form import UserCreateForm, ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from user.models import Account, Categories
from django.forms import ModelForm, widgets

# Create your views here.


def index(request):
    return render(request, 'user/index.html',{
        'user': Account.objects.all()
    })


# def create_user(request):
#     if request.method == 'POST':
#         form = UserCreateForm(data=request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect('event-index')
#     else:
#         form = UserCreateForm()
#     return render(request, 'user/create_user.html', {
#         'form': form
#     })


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreateForm()
    })


def profile(request):
    profile = Account.objects.filter(id=request.user.id).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile),
        'user': profile
        # 'categories': Categories.objects.all()
    })