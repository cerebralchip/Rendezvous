from django import forms
from .models import Post, Profile
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    Text = forms.CharField(label='Post Content')
    
    class Meta:
        model = Post
        fields = ['Picture', 'Title', 'Text', 'CountryID', 'Tags']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('Bio', 'Picture', 'BornInCountryID', 'LivingInCountryID',)