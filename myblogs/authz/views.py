from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import View
from django.urls import reverse
from django.views import generic
from .forms import SignupForm



# Create your views here.
class UserRegister(generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')