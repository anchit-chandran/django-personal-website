# Std Lib imports

# 3rd Party imports
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import frontmatter
import markdown as md

# Personal imports
from .models import (
    BlogPost,
    Project,
)
from .general_functions import (
    calculate_reading_time,
)
from .constants import (
    DEFAULT_HEADER_IMG_URL,
)


# Create your views here.
def index(request):
    # get blog posts
    if BlogPost.objects.filter(featured=True).count() >= 3:
        featured_blog_posts = BlogPost.objects.filter(featured=True)
    else:
        featured_blog_posts = BlogPost.objects.all()[:3]

    # get projects
    if Project.objects.filter(featured=True).count() >= 3:
        featured_projects = Project.objects.filter(featured=True)
    else:
        featured_projects = Project.objects.all()[:3]
    
    # get just the first para from the md content
    for project in featured_projects:
        md_html = md.markdown(project.content)
        p_close_tag_index = md_html.find('</p>')+4
        projects_first_p = md_html[:p_close_tag_index]
        
        # assign to python project object .content attribute
        project.content = projects_first_p
        
    return render(
        request,
        "app_website/index.html",
        {
            "posts": featured_blog_posts,
            "projects" : featured_projects,
            "projects_first_p" : projects_first_p,
            "DEFAULT_HEADER_IMG_URL": DEFAULT_HEADER_IMG_URL.DEFAULT_HEADER_IMG_URL,
        },
    )


def view_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)

    reading_time = calculate_reading_time(post.content)
    return render(
        request, "app_website/post.html", {"post": post, "reading_time": reading_time}
    )

def view_project(request, project_id):
    
    project = Project.objects.get(id=project_id)
    
    return render(
        request, "app_website/project.html", {"project": project}
    )

def about(request):
    return render(request, "app_website/about.html")


def projects(request):
    
    projects = Project.objects.all()
    
    # get just the first para from the md content
    for project in projects:
        md_html = md.markdown(project.content)
        p_close_tag_index = md_html.find('</p>')+4
        projects_first_p = md_html[:p_close_tag_index]
        
        # assign to python project object .content attribute
        project.content = projects_first_p
    
    return render(request, "app_website/projects.html", {"projects":projects})


def blog(request):
    posts = BlogPost.objects.all().order_by("-posted_at")
    return render(request, "app_website/blog.html", {"posts": posts})


def contact(request):
    return render(request, "app_website/contact.html")
