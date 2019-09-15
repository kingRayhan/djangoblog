from django.shortcuts import render
from .models import Blog
# Create your views here.


def index(request):
    posts = Blog.objects.all()
    return render(request, 'blog/index.html', {"posts": posts})


def single(request, slug):
    post = Blog.objects.get(slug=slug)
    return render(request, 'blog/single.html', {"post": post})
