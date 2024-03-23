"""
URL configuration for rendezvous project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

from rendezvous_app import views


from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views




urlpatterns = [
    path("", views.index, name="index"),
    path("map/", views.map, name="map"),
    path("discover/", views.discover, name="discover"),
    path("resources/<str:country>", views.resources, name="resources"),

    path('accounts/<int:user_id>/', views.profile, name='profile_with_id'),
    path('accounts/profile/', views.current_user_profile, name='profile'),

    path("settings/", views.settings, name="settings"),
    path("about/", views.about, name="about"),


    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path("register/", views.register, name="register"),

    path("country/", views.country, name="country"),
    path("search/", views.search, name="search"),
    path("search_results/", views.search_results, name="search_results"),

    path("comment/", views.comment, name="comment"),
    path('post/<int:post_id>/comment/', views.comment, name='comment'),
    path("admin/", admin.site.urls),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path('create_post/', views.create_post, name='create_post'),

    path('post/<int:post_id>/upvote/', views.upvote_post, name='upvote_post'),
    path('post/<int:post_id>/downvote/', views.downvote_post, name='downvote_post'),
    path('comment/<int:comment_id>/upvote/', views.upvote_comment, name='upvote_comment'),
    path('comment/<int:comment_id>/downvote/', views.downvote_comment, name='downvote_comment'),

    path('api/recent-posts/', views.get_recent_posts, name='recent-posts'),
    path('api/popular-posts/', views.get_popular_posts, name='popular-posts'),
    path('api/featured-posts/', views.get_featured_posts, name='featured-posts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)