from django.shortcuts import render
from django.http import HttpResponse

from rendezvous_app.models import Country, Post

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

# Define the login view
def login(request):
    # Add your logic here
    return render(request, 'rendezvous/login.html')

# Define the register view
def register(request):
    # Add your logic here
    return render(request, 'rendezvous/register.html')

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

# You would also have to include imports for models if you interact with the database
