from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.core import serializers

from rendezvous_app.models import Country, Post, Profile, Comment, Tag
from .forms import UserForm, UserProfileForm, PostForm

import json

# Define the home view
def index(request):
    return render(request, 'rendezvous/index.html')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.UserID = request.user
            post.save()  # Save the post to generate the PostID
            
            new_tags = form.cleaned_data.get('new_tags', '').split(',')
            for tag_name in new_tags:
                tag_name = tag_name.strip()
                if tag_name:
                    tag, _ = Tag.objects.get_or_create(TagName=tag_name)
                    post.Tags.add(tag)  # Add the tags after saving the post
            
            return redirect('post_detail', post_id=post.PostID)
    else:
        form = PostForm()
    return render(request, 'rendezvous/create_post.html', {'form': form})

def post_detail(request, post_id):
    post = get_object_or_404(Post, PostID=post_id)
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
def resources(request, country):
    # Query db for all posts with relevant country tag
    posts = Post.objects.filter(CountryID__CountryName=country)
    # Get posts with containing tags
    guides_and_tips = []
    eats = []
    stays = []
    language = []
    for post in posts:
        # limit post text to 100 characters
        post.Text = post.Text[:100] + '...' if len(post.Text) > 100 else post.Text
        if post.Tags.filter(TagName='guides and tips').exists():
            if len(guides_and_tips) < 4:
                guides_and_tips.append(post)
        if post.Tags.filter(TagName='eats').exists() or post.Tags.filter(TagName='food').exists() or post.Tags.filter(TagName='restaurant').exists() or post.Tags.filter(TagName='cafe').exists() or post.Tags.filter(TagName='bar').exists() or post.Tags.filter(TagName='pub').exists() or post.Tags.filter(TagName='street food').exists() or post.Tags.filter(TagName='market').exists() or post.Tags.filter(TagName='bakery').exists() or post.Tags.filter(TagName='grocery').exists() or post.Tags.filter(TagName='supermarket').exists() or post.Tags.filter(TagName='food truck').exists() or post.Tags.filter(TagName='food court').exists() or post.Tags.filter(TagName='food stall').exists():
            if len(eats) < 4:
                eats.append(post)
        if post.Tags.filter(TagName='stays').exists() or post.Tags.filter(TagName='accommodation').exists() or post.Tags.filter(TagName='lodging').exists() or post.Tags.filter(TagName='hotel').exists() or post.Tags.filter(TagName='hostel').exists() or post.Tags.filter(TagName='bnb').exists() or post.Tags.filter(TagName='airbnb').exists() or post.Tags.filter(TagName='couchsurfing').exists() or post.Tags.filter(TagName='camping').exists() or post.Tags.filter(TagName='glamping').exists() or post.Tags.filter(TagName='resort').exists() or post.Tags.filter(TagName='motel').exists() or post.Tags.filter(TagName='inn').exists() or post.Tags.filter(TagName='guesthouse').exists() or post.Tags.filter(TagName='apartment').exists() or post.Tags.filter(TagName='villa').exists():
            if len(stays) < 4:
                stays.append(post)
        if post.Tags.filter(TagName='language').exists():
            if len(language) < 4:
                language.append(post)

    return render(request, 'rendezvous/resources.html', {'country': country, 'guides_and_tips': guides_and_tips, 'eats': eats, 'stays': stays, 'language': language, 'active_page': 'resources'})

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
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'rendezvous/login.html', {'form': form, 'active_page': 'login'})

# define logout view
def logout_view(request):
        logout(request)
        return redirect('index')

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
    # get querystring from request
    query = request.GET.get('query')
    posts = []
    # if query is not empty
    if query:
        # get posts with tags containing query lowercase
        posts = Post.objects.filter(Tags__TagName__icontains=query.lower())
        # append posts with country name containing query
        posts = posts | Post.objects.filter(CountryID__CountryName__icontains=query)
        # append posts with title or text containing query
        posts = posts | Post.objects.filter(Title__icontains=query) | Post.objects.filter(Text__icontains=query)
        
    return render(request, 'rendezvous/search_results.html', {'posts': posts, 'query': query})

# Define the search_results view
def search_results(request):
    # Add your logic here
    return render(request, 'rendezvous/search_results.html')

def comment(request, post_id):
    post = get_object_or_404(Post, PostID=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            comment = Comment(
                Content=content,
                UserID=request.user,
                PostID=post
            )
            comment.save()
    return redirect('post_detail', post_id=post_id)

def upvote_post(request, post_id):
    post = get_object_or_404(Post, PostID=post_id)
    user = request.user

    if user.is_authenticated:
        if user in post.upvoted_by.all():
            post.Upvotes -= 1
            post.upvoted_by.remove(user)
        else:
            if user in post.downvoted_by.all():
                post.Downvotes -= 1
                post.downvoted_by.remove(user)
            post.Upvotes += 1
            post.upvoted_by.add(user)
        post.save()

    return redirect('post_detail', post_id=post_id)

def downvote_post(request, post_id):
    post = get_object_or_404(Post, PostID=post_id)
    user = request.user

    if user.is_authenticated:
        if user in post.downvoted_by.all():
            post.Downvotes -= 1
            post.downvoted_by.remove(user)
        else:
            if user in post.upvoted_by.all():
                post.Upvotes -= 1
                post.upvoted_by.remove(user)
            post.Downvotes += 1
            post.downvoted_by.add(user)
        post.save()

    return redirect('post_detail', post_id=post_id)

def upvote_comment(request, comment_id):
    comment = get_object_or_404(Comment, CommentID=comment_id)
    user = request.user

    if user.is_authenticated:
        if user in comment.upvoted_by.all():
            comment.Upvotes -= 1
            comment.upvoted_by.remove(user)
        else:
            if user in comment.downvoted_by.all():
                comment.Downvotes -= 1
                comment.downvoted_by.remove(user)
            comment.Upvotes += 1
            comment.upvoted_by.add(user)
        comment.save()

    return redirect('post_detail', post_id=comment.PostID.PostID)

def downvote_comment(request, comment_id):
    comment = get_object_or_404(Comment, CommentID=comment_id)
    user = request.user

    if user.is_authenticated:
        if user in comment.downvoted_by.all():
            comment.Downvotes -= 1
            comment.downvoted_by.remove(user)
        else:
            if user in comment.upvoted_by.all():
                comment.Upvotes -= 1
                comment.upvoted_by.remove(user)
            comment.Downvotes += 1
            comment.downvoted_by.add(user)
        comment.save()

    return redirect('post_detail', post_id=comment.PostID.PostID)


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

