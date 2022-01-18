from django import forms
from .models import BlogPost, Comment, Genre
from ckeditor.fields import RichTextField

def get_my_choices():
    choices = Genre.objects.all().values_list('name', 'name')
    return choices
  
class BlogPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BlogPostForm, self).__init__(*args, **kwargs)
        self.fields['genre'] = forms.ChoiceField(required=True,
                              choices=get_my_choices(),
                              widget=forms.Select(attrs={'class': 'form-select'}))

    title = forms.CharField(required=True,
                            max_length=200,
                            widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}))
    post = RichTextField()

    # post = forms.CharField(required=True,
    #                        widget=forms.Textarea(attrs={'placeholder': 'write something...', 'class': 'form-control'}))

    class Meta:
        model = BlogPost
        fields = ('title', 'genre', 'post')
        exclude = ('created_on', 'updated_on', 'author')


class CommentForm(forms.ModelForm):

    comment = forms.CharField(required=True,
                              widget=forms.Textarea(attrs={'placeholder': 'write your comment',
                                                            'row': 25, 'col': 25, 'class': 'form-control'}))

    class Meta:
        model = Comment
        fields = ('comment',)
        exclude = ('created_on',)
