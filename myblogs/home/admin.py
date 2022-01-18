from django.contrib import admin

from .models import BlogPost, Comment, Genre

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Genre)
admin.site.register(Comment)
