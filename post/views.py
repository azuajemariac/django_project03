from django.shortcuts import render
from django.views.generic import ListView
from post.models import post

# Create your views here.

class PostListView(ListView):
    model=post
    template_name='post.html'

