"""myblogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('blogs/', views.BlogPostList.as_view(), name='blogposts'),
    path('blog/<int:pk>/', views.BlogPostDetail.as_view(), name='blogpost-detail-view'),
    path('blog/post/', views.AddBlogPost.as_view(), name='add-post'),
    path('blog/edit/<int:pk>/', views.EditBlogPost.as_view(), name='edit-post'),
    path('blogs/<int:pk>/delete/', views.DeleteBlogPost.as_view(), name="delete-post"),
    path('blog/genre/', views.AddBlogPostGenre.as_view(), name='add-genre'),
    path('blog/genre/<str:genre>', views.genre_view, name='genre'),
    path('like/<int:pk>/', views.blogpost_like, name='blogpost-like'),

]
