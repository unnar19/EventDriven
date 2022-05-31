from django.contrib.auth.forms import UserCreationForm, User
from django.forms import ModelForm, widgets
from django import forms
from user.models import Account


class UserCreateForm(UserCreationForm):
    class Meta:
        model = Account
        fields = UserCreationForm.Meta.fields + ('email','first_name','last_name','image_url')
        exclude = ['id']
        widgets = {
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'image_url': widgets.TextInput(attrs={'class': 'form-control'})
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Account
        fields = ('fav_cat','image_url','username')
        exclude = ['id', 'user']
        widgets = {
            'favorite_event': widgets.Select(attrs={'class': 'form-control'}),
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'})
        }