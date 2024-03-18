from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    CountryID = models.IntegerField()
    CountryName = models.CharField(max_length=100)

    def __str__(self):
        return self.CountryName

    class Meta:
        verbose_name_plural = 'countries'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    BornInCountryID = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='born_users')
    LivingInCountryID = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='living_users')
    Picture = models.ImageField()
    Bio = models.CharField(max_length=500)

    def __str__(self):
        return self.Username




class Post(models.Model):
    # prost id, primary key
    PostID = models.IntegerField()
    Picture = models.ImageField()
    Text = models.CharField(max_length=1000)
    Upvotes = models.IntegerField(default=0)  # Provide a default value
    Downvotes = models.IntegerField(default=0)  # Provide a default value
    CountryID = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='posts')
    Tags = models.ManyToManyField('Tag', related_name='posts')
    is_featured = models.BooleanField(default=False)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post ID: {self.PostID}"

class Tag(models.Model):
    TagID = models.IntegerField()
    TagName = models.CharField(max_length=30)

    def __str__(self):
        return self.TagName

class Comment(models.Model):
    CommentID = models.IntegerField()
    Content = models.CharField(max_length=280)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    Upvotes = models.IntegerField()
    Downvotes = models.IntegerField()
    PostID = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"Comment ID: {self.CommentID}"