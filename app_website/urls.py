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
    path("admin/login", views.login_user, name="login_user"),
    path("admin/logout", views.logout_user, name="logout_user"),
    path("admin/view-actions", views.admin_user_view, name="admin_user_view"),
    path("admin/blog/post/create", views.create_draft_post, name="create_draft_post"),
    path("admin/blog/view", views.view_posts_admin, name="view_posts_admin"),
    path("admin/projects/view", views.view_projects_admin, name="view_projects_admin"),
    path("admin/blog/post/publish/<int:post_id>", views.publish_draft_post, name="publish_draft_post"),
    path("admin/blog/post/edit_post/<int:post_id>", views.edit_post, name="edit_post"),
    path("admin/subscribers", views.view_subscribers, name="view_subscribers"),
    path(
        "admin/subscriber/edit/<int:subscriber_id>",
        views.edit_subscriber,
        name="edit_subscriber",
    ),
]
