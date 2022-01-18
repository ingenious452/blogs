from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets


class SignupForm(UserCreationForm):
    
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'email', 'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)  # call the actual user creation form and set the inputs

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

