from django.contrib.auth.forms import UserCreationForm, User
from django.forms import ModelForm, widgets
from django import forms
from user.models import Account, Categories


class UserCreateForm(UserCreationForm):
    class Meta:
        model = Account
        fields = UserCreationForm.Meta.fields + ('email','first_name','last_name','image_url')
        exclude = ['id']
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            # 'image': widgets.ClearableFileInput(attrs={'class': 'form-control'})
            'image_url': widgets.TextInput(attrs={'class': 'form-control',})
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Account
        fields = ( 'image_url', 'username','fav_cat')
        labels = {
            "fav_cat":"Favourite category"
        }
        help_texts = {
            'username': None
        }
        exclude = ['id', 'user']
        widgets = {
            'favorite_event': widgets.Select(attrs={'class': 'form-control cat_select'}),
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'})
        }