from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile, Post, Comment, Country

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create Country objects for the Profile and Post
        self.country1 = Country.objects.create(CountryName='Country 1')
        self.country2 = Country.objects.create(CountryName='Country 2')
        
        self.profile = Profile.objects.create(
            user=self.user,
            BornInCountryID=self.country1,
            LivingInCountryID=self.country2
        )
        self.post = Post.objects.create(
            UserID=self.user,
            Title='Test Post',
            Text='This is a test post.',
            CountryID=self.country1  # Assign a valid CountryID to the Post
        )

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rendezvous/index.html')

    def test_create_post_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('create_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rendezvous/create_post.html')

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.PostID]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rendezvous/post_detail.html')

    def test_upvote_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('upvote_post', args=[self.post.PostID]))
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.Upvotes, 1)

    def test_comment_creation(self):
        self.client.login(username='testuser', password='testpassword')
        data = {'content': 'This is a test comment.'}
        response = self.client.post(reverse('comment', args=[self.post.PostID]), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.count(), 1)

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create Country objects for the Profile and Post
        self.country1 = Country.objects.create(CountryName='Country 1')
        self.country2 = Country.objects.create(CountryName='Country 2')
        
        self.profile = Profile.objects.create(
            user=self.user,
            BornInCountryID=self.country1,
            LivingInCountryID=self.country2
        )
        self.post = Post.objects.create(
            UserID=self.user,
            Title='Test Post',
            Text='This is a test post.',
            CountryID=self.country1  # Assign a valid CountryID to the Post
        )

    def test_profile_creation(self):
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(self.profile.user, self.user)

    def test_post_creation(self):
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(self.post.UserID, self.user)
        self.assertEqual(self.post.Title, 'Test Post')
        self.assertEqual(self.post.Text, 'This is a test post.')

    def test_comment_creation(self):
        comment = Comment.objects.create(UserID=self.user, PostID=self.post, Content='This is a test comment.')
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(comment.UserID, self.user)
        self.assertEqual(comment.PostID, self.post)
        self.assertEqual(comment.Content, 'This is a test comment.')