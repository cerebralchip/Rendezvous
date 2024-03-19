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
    path("", views.home, name="home"),
    path("map/", views.map, name="map"),
    path("discover/", views.discover, name="discover"),
    path("resources/", views.resources, name="resources"),

    path('accounts/profile/', views.profile, name='profile'),

    path("settings/", views.settings, name="settings"),
    path("about/", views.about, name="about"),


    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path("register/", views.register, name="register"),

    path("country/", views.country, name="country"),
    path("search/", views.search, name="search"),
    path("search_results/", views.search_results, name="search_results"),
    path("comment/", views.comment, name="comment"),
    path("admin/", admin.site.urls),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path('create_post/', views.create_post, name='create_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)