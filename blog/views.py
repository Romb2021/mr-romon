from django.shortcuts import render, redirect
from .models import BlogPost

def blog_index(request):
    posts = BlogPost.objects.order_by('-timestamp')
    return render(request, 'blog/blog_index.html',{'posts': posts})