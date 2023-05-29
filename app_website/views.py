from django.shortcuts import render
from django.http import HttpResponse

from .models import (
    BlogPost,
)


# Create your views here.
def index(request):
    featured_blog_posts = BlogPost.objects.filter(featured=True)

    return render(request, "app_website/index.html", {"posts": featured_blog_posts})


def view_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    return render(request, "app_website/post.html", {'post':post})


def about(request):
    return render(request, "app_website/about.html")


def projects(request):
    return render(request, "app_website/projects.html")


def blog(request):
    posts = BlogPost.objects.all().order_by('-posted_at')
    return render(request, "app_website/blog.html", {'posts':posts})


def contact(request):
    return render(request, "app_website/contact.html")
