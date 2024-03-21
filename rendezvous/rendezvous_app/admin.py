from django.contrib import admin
from .models import Country, User, Post, Tag, Comment

class CountryAdmin(admin.ModelAdmin):
    list_display = ('CountryID', 'CountryName')

class PostAdmin(admin.ModelAdmin):
    list_display = ('PostID', 'Text', 'CountryID', 'published_date')
    list_filter = ('is_featured', 'published_date', 'CountryID')
    search_fields = ('Text',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('TagID', 'TagName')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('CommentID', 'Content', 'UserID', 'PostID')
    search_fields = ('Content',)

admin.site.register(Country, CountryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
