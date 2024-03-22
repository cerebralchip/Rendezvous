from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



from django.core import serializers

from rendezvous_app.models import Country, Post, Profile
from .forms import UserForm, UserProfileForm, PostForm

import json

# Define the home view
def index(request):
    # Fetch featured and recent posts from the database
    featured_posts = Post.objects.filter(is_featured=True).order_by('-published_date')[:3]
    recent_posts = Post.objects.order_by('-published_date')[:5]
    # Fetch a list of countries, maybe for a dropdown or list in the UI
    countries = Country.objects.all()
    
    # Construct the context with the fetched data
    context = {
        'featured_posts': featured_posts,
        'recent_posts': recent_posts,
        'countries': countries
    }
    
    # Render and return the response, passing in the context data
    return render(request, 'rendezvous/index.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'rendezvous/create_post.html', {'form': form})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'rendezvous/post_detail.html', {'post': post})

# Define the map view
def map(request):
    # Add your logic here
    return render(request, 'rendezvous/map.html')

# Define the discover view
def discover(request):
    # Add your logic here
    return render(request, 'rendezvous/discover.html', {'active_page': 'discover'})

# Define the resources view
def resources(request):
    # Add your logic here
    return render(request, 'rendezvous/resources.html', {'active_page': 'resources'})

# Define the profile view
def profile(request):
    # Add your logic here
    return render(request, 'rendezvous/profile.html')

# Define the settings view
def settings(request):
    # Add your logic here
    return render(request, 'rendezvous/settings.html')

# Define the about view
def about(request):
    # Add your logic here
    return render(request, 'rendezvous/about.html', {'active_page': 'about'})

# define login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'rendezvous/login.html', {'form': form, 'active_page': 'login'})

# define logout view
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            login(request, user)
            return redirect('index')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'rendezvous/register.html', {'user_form': user_form, 'profile_form': profile_form})

# Define the country view
def country(request):
    # Add your logic here
    return render(request, 'rendezvous/country.html')

# Define the search view
def search(request):
    # Add your logic here
    return render(request, 'rendezvous/search.html')

# Define the search_results view
def search_results(request):
    # Add your logic here
    return render(request, 'rendezvous/search_results.html')

# Define the comment view
def comment(request):
    # Add your logic here
    return HttpResponse("This is where comments are handled.")


################# API Views #################

def get_posts(order_by, num_posts):
    posts = Post.objects.order_by(*order_by)[:num_posts]
    posts_json = serializers.serialize('json', posts)
    posts_data = json.loads(posts_json)
    
    for post in posts_data:
        user_id = post['fields']['UserID']
        user = User.objects.get(id=user_id)
        username = user.username
        post['fields']['username'] = username
    
    return json.dumps(posts_data)

# Get Recent posts as used in discover page
def get_recent_posts(request):
    recent_posts_json = get_posts(['-published_date'], 3)
    return HttpResponse(recent_posts_json, content_type='application/json')

# Get most popular posts (i.e. posts with the most upvotes)
def get_popular_posts(request):
    popular_posts_json = get_posts(['-Upvotes'], 3)
    return HttpResponse(popular_posts_json, content_type='application/json')

# # Get posts with is_featured set to True
def get_featured_posts(request):
    # Filter posts with is_featured set to True
    featured_posts = Post.objects.filter(is_featured=True)

    # Serialize the queryset
    featured_posts_json = serializers.serialize('json', featured_posts)

    # Return the JSON response
    return HttpResponse(featured_posts_json, content_type='application/json')

