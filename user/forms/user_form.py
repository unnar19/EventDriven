from django.forms import ModelForm, widgets
from django import forms
from user.models import Account


class UserCreateForm(ModelForm):
    class Meta:
        model = Account
        exclude = ['id']
        widgets = {
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'password': widgets.TextInput(attrs={'class': 'form-control'}),
            'image_url': widgets.TextInput(attrs={'class': 'form-control'})
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Account
        exclude = ['id', 'user']
        widgets = {
            'favorite_event': widgets.Select(attrs={'class': 'form-control'}),
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'})
        }