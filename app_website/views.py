# Std Lib imports

# 3rd Party imports
from django.shortcuts import render, redirect
import markdown as md
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Personal imports
from .models import (
    BlogPost,
    Project,
    Subscribers,
)
from .constants import (
    DEFAULT_HEADER_IMG_URL,
)
from .forms import LoginForm, CreateDraftPostForm, PublishPostForm


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
        p_close_tag_index = md_html.find("</p>") + 4
        projects_first_p = md_html[:p_close_tag_index]

        # assign to python project object .content attribute
        project.content = projects_first_p

    return render(
        request,
        "app_website/index.html",
        {
            "posts": featured_blog_posts,
            "projects": featured_projects,
            "DEFAULT_HEADER_IMG_URL": DEFAULT_HEADER_IMG_URL.DEFAULT_HEADER_IMG_URL,
        },
    )


def view_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    
    return render(
        request, "app_website/post.html", {"post": post}
    )


def view_project(request, project_id):
    project = Project.objects.get(id=project_id)

    return render(request, "app_website/project.html", {"project": project})


def about(request):
    return render(request, "app_website/about.html")


def projects(request):
    projects = Project.objects.all()

    # get just the first para from the md content
    for project in projects:
        md_html = md.markdown(project.content)
        p_close_tag_index = md_html.find("</p>") + 4
        projects_first_p = md_html[:p_close_tag_index]

        # assign to python project object .content attribute
        project.content = projects_first_p

    return render(request, "app_website/projects.html", {"projects": projects})


def blog(request):
    posts = BlogPost.objects.filter(published=True).order_by("-posted_at")
    return render(request, "app_website/blog.html", {"posts": posts})


def contact(request):
    return render(request, "app_website/contact.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect("index")

    form = LoginForm()

    return render(request, "app_website/login.html", {"form": form})


@login_required
def logout_user(request):
    logout(request)

    return redirect("index")


@login_required
def admin_user_view(request):
    return render(request, "app_website/admin_user_view.html")


@login_required
def create_draft_post(request):
    if request.method == "POST":
        form = CreateDraftPostForm(request.POST, initial={"published": False})

        if form.is_valid():
            form.save()
            return redirect("view_draft_posts")

    form = CreateDraftPostForm()

    return render(request, "app_website/create_post.html", {"form": form})


@login_required
def view_draft_posts(request):
    draft_posts = BlogPost.objects.filter(published=False)

    return render(request, "app_website/view_draft_posts.html", {"posts": draft_posts})


@login_required
def edit_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)

    if request.method == "POST":
        form = CreateDraftPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("view_post", post_id=post_id)

    form = CreateDraftPostForm(instance=post)

    return render(request, "app_website/edit_post.html", {"form": form})


@login_required
def publish_draft_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    
    subscriber_count = Subscribers.objects.filter(subscribed=True).count()

    if request.method == "POST":
        form = PublishPostForm(request.POST)

        if form.is_valid():
            if form.cleaned_data["confirm_publish"]:
                # publish post onto website
                post_to_publish = BlogPost.objects.get(id=post_id)
                post_to_publish.published = True
                post_to_publish.save()

                html_content = md.markdown(post_to_publish.content)

                # format meta content
                post_to_publish.posted_at = post_to_publish.posted_at.strftime(
                    "%-d %b %Y"
                )
                post.reading_time = post.calculate_reading_time()
                
                meta_content = f'<p class="text-center"><small>{ post_to_publish.posted_at} • Reading time: {post.reading_time} mins</small></p>'

                # get img
                img = f'<img src="{ post.header_img }" style="height: 250px; width: 250px; margin-right: auto; margin-left: auto;">'

                # put message together for email in html format
                message = meta_content + "\n" + img + "\n" + html_content
                
                # get subscribers
                subscribers = list(Subscribers.objects.filter(subscribed=True).values_list("email", flat=True))

                send_mail(
                    subject=post_to_publish.title,
                    message=post_to_publish.content,
                    html_message=message,
                    from_email="anchit97123@gmail.com",
                    recipient_list=subscribers,
                    fail_silently=False,
                )

                return redirect("blog")

    form = PublishPostForm()
    return render(
        request, "app_website/publish_draft_post.html", {"post": post, "form": form, "subscriber_count":subscriber_count}
    )
