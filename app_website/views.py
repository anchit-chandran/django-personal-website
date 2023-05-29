from django.shortcuts import render
from django.http import HttpResponse

from .models import (
    BlogPost,
)
from .general_functions import (
    calculate_reading_time,
)
from .constants import DEFAULT_HEADER_IMG_URL

# Create your views here.
def index(request):

    if BlogPost.objects.filter(featured=True).exists():
        featured_blog_posts = BlogPost.objects.filter(featured=True)
    else:
        featured_blog_posts = BlogPost.objects.all()[:3]
        
        
    return render(request, "app_website/index.html", {"posts": featured_blog_posts, 'DEFAULT_HEADER_IMG_URL': DEFAULT_HEADER_IMG_URL.DEFAULT_HEADER_IMG_URL})


def view_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)

    reading_time = calculate_reading_time(post.content)
    return render(request, "app_website/post.html", {'post':post, 'reading_time':reading_time})


def about(request):
    return render(request, "app_website/about.html")


def projects(request):
    return render(request, "app_website/projects.html")


def blog(request):
    posts = BlogPost.objects.all().order_by('-posted_at')
    return render(request, "app_website/blog.html", {'posts':posts})


def contact(request):
    return render(request, "app_website/contact.html")
