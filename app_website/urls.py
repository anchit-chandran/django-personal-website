from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("projects", views.projects, name="projects"),
    path("projects/<int:project_id>", views.view_project, name="view_project"),
    path("blog", views.blog, name="blog"),
    path("blog/post/<int:post_id>", views.view_post, name='view_post'),
    path("contact", views.contact, name="contact"),
    path("login", views.login_user, name="login_user"),
    path("logout", views.logout_user, name="logout_user"),
    path("admin_user", views.admin_user_view, name="admin_user_view"),
    path("create_draft_post", views.create_draft_post, name="create_draft_post"),
    path("view_draft_posts", views.view_draft_posts, name="view_draft_posts"),
    path("publish/<int:post_id>", views.publish_draft_post, name="publish_draft_post"),
]
