from django.db import models

class Country(models.Model):
    CountryID = models.IntegerField()
    CountryName = models.CharField(max_length=100)

class User(models.Model):
    UserID = models.IntegerField()
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    BornInCountryID = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='born_users')
    LivingInCountryID = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='living_users')
    Picture = models.ImageField()
    Bio = models.CharField(max_length=500)

class Post(models.Model):
    PostID = models.IntegerField()
    Picture = models.ImageField()
    Text = models.CharField(max_length=1000)
    Upvotes = models.IntegerField()
    Downvotes = models.IntegerField()
    CountryID = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='posts')
    Tags = models.ManyToManyField('Tag', related_name='posts')

class Tag(models.Model):
    TagID = models.IntegerField()
    TagName = models.CharField(max_length=30)

class Comment(models.Model):
    CommentID = models.IntegerField()
    Content = models.CharField(max_length=280)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    Upvotes = models.IntegerField()
    Downvotes = models.IntegerField()
    PostID = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
