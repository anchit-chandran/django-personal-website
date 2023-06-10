from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("projects", views.projects, name="projects"),
    path("projects/<int:project_id>", views.view_project, name="view_project"),
    path("blog", views.blog, name="blog"),
    path("blog/post/<int:post_id>", views.view_post, name="view_post"),
    path("contact", views.contact, name="contact"),
    path("login", views.login_user, name="login_user"),
    path("logout", views.logout_user, name="logout_user"),
    path("admin_user", views.admin_user_view, name="admin_user_view"),
    path("create_draft_post", views.create_draft_post, name="create_draft_post"),
    path("admin/view_posts", views.view_posts_admin, name="view_posts_admin"),
    path("publish/<int:post_id>", views.publish_draft_post, name="publish_draft_post"),
    path("edit_post/<int:post_id>", views.edit_post, name="edit_post"),
    path("subscribers", views.view_subscribers, name="view_subscribers"),
    path(
        "subscriber/edit/<int:subscriber_id>",
        views.edit_subscriber,
        name="edit_subscriber",
    ),
]
