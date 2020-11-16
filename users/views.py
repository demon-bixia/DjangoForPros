from django.shortcuts import render
from django.views import generic
from .forms import CustomUserCreationForm, UserCreationForm
from django.urls import reverse_lazy


class SignUpPageView(generic.CreateView):
    form_class=CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
