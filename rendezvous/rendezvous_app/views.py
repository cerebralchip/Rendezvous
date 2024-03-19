from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from rendezvous_app.models import Country, Post
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


from .forms import PostForm

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
    return render(request, 'rendezvous/login.html', {'form': form})

# define logout view
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

# Define the home view
def home(request):
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
    return render(request, 'rendezvous/home.html', context)

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
    return render(request, 'rendezvous/discover.html')

# Define the resources view
def resources(request):
    # Add your logic here
    return render(request, 'rendezvous/resources.html')

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
    return render(request, 'rendezvous/about.html')

# Define the register view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'rendezvous/register.html', {'form': form})

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

