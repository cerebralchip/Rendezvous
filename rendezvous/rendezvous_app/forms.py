from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    Text = forms.CharField(label='Post Content')
    
    class Meta:
        model = Post
        fields = ['Picture', 'Text', 'CountryID', 'Tags']