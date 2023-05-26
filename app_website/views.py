from django.shortcuts import render
from django.http import HttpResponse

from .models import (
    BlogPost,
)

# Create your views here.
def index(request):
    
    blog_posts = BlogPost.objects.filter(featured=True)
    
    return render(request, 'app_website/index.html', {
        'posts' : blog_posts 
    })