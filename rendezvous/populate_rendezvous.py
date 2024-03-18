import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rendezvous.settings')
django.setup()

from rendezvous_app.models import Country, Profile, Post, Tag, Comment
from django.contrib.auth.models import User

def populate():
    # Create countries
    countries = [
        {'CountryID': 1, 'CountryName': 'United States'},
        {'CountryID': 2, 'CountryName': 'United Kingdom'},
        {'CountryID': 3, 'CountryName': 'France'},
        # Add more countries as needed
    ]

    for country_data in countries:
        Country.objects.get_or_create(**country_data)

    # Create users
    profiles = [
        {'username': 'user1', 'BornInCountryID_id': 1, 'LivingInCountryID_id': 1, 'Picture': 'profile_pics/user1.jpg', 'Bio': 'I love to travel!'},
        {'username': 'user2', 'BornInCountryID_id': 2, 'LivingInCountryID_id': 2, 'Picture': 'profile_pics/user2.jpg', 'Bio': 'I am a foodie!'},
        # Add more users as needed
    ]

    for profile_data in profiles:
        user, created = User.objects.get_or_create(username=profile_data['username'])
        if created:
            user.set_password('12345')  # Set a default password
            user.save()
        profile_data.pop('username')  # Remove the username field
        profile, created = Profile.objects.get_or_create(user=user, **profile_data)

    # Create tags
    tags = [
        {'TagID': 1, 'TagName': 'Adventure'},
        {'TagID': 2, 'TagName': 'Culture'},
        {'TagID': 3, 'TagName': 'Food'},
        # Add more tags as needed
    ]

    for tag_data in tags:
        Tag.objects.get_or_create(**tag_data)

    # Create posts
    posts = [
        {'PostID': 1, 'Text': 'Amazing trip to the mountains!', 'Upvotes': 10, 'Downvotes': 0, 'CountryID_id': 1, 'is_featured': True},
        {'PostID': 2, 'Text': 'Delicious cuisine in Paris', 'Upvotes': 5, 'Downvotes': 1, 'CountryID_id': 3, 'is_featured': False},
        # Add more posts as needed
    ]

    for post_data in posts:
        post, _ = Post.objects.get_or_create(**post_data)
        post.Tags.set([Tag.objects.get(TagID=1), Tag.objects.get(TagID=3)])

    # Create comments
    comments = [
        {'CommentID': 1, 'Content': 'Great post!', 'UserID_id': 2, 'Upvotes': 3, 'Downvotes': 0, 'PostID_id': 1},
        {'CommentID': 2, 'Content': 'I want to visit there too', 'UserID_id': 1, 'Upvotes': 2, 'Downvotes': 0, 'PostID_id': 2},
        # Add more comments as needed
    ]

    for comment_data in comments:
        Comment.objects.get_or_create(**comment_data)

if __name__ == '__main__':
    print('Starting population script...')
    populate()
    print('Population script completed.')