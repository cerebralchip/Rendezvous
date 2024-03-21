from django import forms
from .models import Post, Profile

class PostForm(forms.ModelForm):
    Text = forms.CharField(label='Post Content')
    
    class Meta:
        model = Post
        fields = ['Picture', 'Text', 'CountryID', 'Tags']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'picture', 'born_in_country', 'living_in_country',)