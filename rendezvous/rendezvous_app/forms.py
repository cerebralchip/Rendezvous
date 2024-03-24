from django import forms
from .models import Post, Profile, Tag
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    new_tags = forms.CharField(label='New Tags', required=False, help_text='Enter comma-separated tags')
    

    Tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, help_text='Hold down "Control", or "Command" on a Mac, to select multiple tags.')

    class Meta:
        model = Post
        fields = ['Picture', 'Title', 'Text', 'CountryID', 'Tags', 'new_tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Tags'].required = False

    def save(self, commit=True):
        post = super().save(commit=commit)
        return post

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('Bio', 'Picture', 'BornInCountryID', 'LivingInCountryID',)