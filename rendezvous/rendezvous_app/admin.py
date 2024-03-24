from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.models import User
from .models import Country, Profile, Post, Tag, Comment

# Unregister the original User admin
admin.site.unregister(User)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'BornInCountryID', 'LivingInCountryID')

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'

admin.site.register(Profile, ProfileAdmin)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('CountryID', 'CountryName')

class UserAdmin(DefaultUserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')

class PostAdmin(admin.ModelAdmin):
    list_display = ('PostID', 'Text', 'CountryID', 'published_date', 'is_featured', 'Upvotes', 'Downvotes')
    list_filter = ('is_featured', 'published_date', 'CountryID')
    search_fields = ('Text',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('TagID', 'TagName')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('CommentID', 'Content', 'UserID', 'PostID', 'Upvotes', 'Downvotes')
    search_fields = ('Content',)

admin.site.register(Country, CountryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(User, UserAdmin)