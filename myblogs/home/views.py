from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from home.models import BlogPost, Comment, Genre
from home.forms import BlogPostForm


# Create your views here

def blogpost_like(request, pk):
    print(request.POST)
    blogpost = get_object_or_404(BlogPost, id=request.POST.get('post_id'))
    blogpost.likes.add(request.user)
    return redirect(reverse('home:blogpost-detail-view', args=[str(pk)]))


class BlogPostList(generic.ListView):
    model = BlogPost
    genre = Genre.objects.all()
    template_name = 'home/index.html'

    def get_context_data(self, *args, **kwargs):
        genres = Genre.objects.all()
        context =  super(BlogPostList, self).get_context_data(*args, **kwargs)
        context['genres'] = genres
        return context


class BlogPostDetail(generic.DetailView):
    model = BlogPost
    
    def get_context_data(self, *args, **kwargs):
        context = super(BlogPostDetail, self).get_context_data(*args, **kwargs)
        post = get_object_or_404(BlogPost, id=self.kwargs['pk'])  # get the post with the primary key of the given post.
        # comments = Comment.objects.filter(blogpost_id=self.kwargs['pk'])
        likes = post.get_likes()
        print(likes)
        context['total_likes'] = likes
        # context['comments'] = comments
        return context


class AddBlogPost(LoginRequiredMixin, generic.CreateView):
    login_url = 'login'
    redirect_field_name = 'home:add-post'
    model = BlogPost
    form_class = BlogPostForm
    # fields = '__all__'
    # fields = ('title', 'post') # not needed as form will take care of it.
    template_name = 'home/blogpost.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditBlogPost(LoginRequiredMixin, generic.UpdateView):
    login_url = 'login'
    redirect_field_name = 'home:edit-post'
    model = BlogPost
    form_class = BlogPostForm
    # fields = ('title', 'post') # not needed as form will take care of it.
    template_name = 'home/edit_post.html'


class DeleteBlogPost(LoginRequiredMixin, generic.DeleteView):
    login_url = 'login'
    redirect_field_name = 'home:delete-post'
    model = BlogPost
    template_name = 'home/delete_post.html'
    success_url = reverse_lazy('home:blogposts')


class AddBlogPostGenre(LoginRequiredMixin, generic.CreateView):
    """
    Required user to be logged in to view the page
    create a form to add genre by using Genre model and set 
    all the field required by the model to create genre.
    """
    # login_url = 'login'
    # redirect_field_name = 'home:add-genre'
    model = Genre
    fields = ('__all__')  # add all the field in 
    template_name = 'home/add_genre.html'
    success_url = reverse_lazy('home:add-post')


def genre_view(request, genre):
    blogs = BlogPost.objects.filter(genre=genre).all()
    print(blogs)
    return render(request, 'home/category.html', context={'genre': genre, 'blogs': blogs})