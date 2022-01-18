from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home:genre', args=[self.name])


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    post = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='blogposts')

    class Meta:
        ordering = ['-created_on', '-updated_on']

    def __str__(self):
        return self.title

    def get_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        """Return absolute url to a specific record."""
        return reverse('home:blogpost-detail-view', args=[str(self.id)])


class Comment(models.Model):
    comment_post = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # if the user is not present keep the comment.
    blogpost = models.ForeignKey('Blogpost', related_name='comments', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)  # add the date and time when the comment is posted.

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.comment_post