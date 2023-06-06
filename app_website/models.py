from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class BlogPost(models.Model):

    posted_at = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ManyToManyField(Category, blank=True, default='Newsletter')
    title = models.CharField(max_length=100, blank=True, null=True)
    header_img = models.URLField(max_length=500, default='https://images.unsplash.com/photo-1559291001-693fb9166cba?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80', null=True)
    content = models.TextField(max_length=10000, blank=True, null=True)
    featured = models.BooleanField(default=False, null=True)
    
    def __str__(self):
        featured = "*" if self.featured else ""
        return f"{featured}Post {self.title} by {self.author}"


class Skill(models.Model):
    
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
class Project(models.Model):

    posted_at = models.DateTimeField(blank=True, auto_now_add=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField(max_length=5000, blank=True, null=True)
    github = models.URLField(blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    featured = models.BooleanField(default=False)
    header_img = models.URLField(max_length=500, default='https://images.unsplash.com/photo-1559291001-693fb9166cba?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80', null=True)
    
    def __str__(self):
        featured = "*" if self.featured else ""
        return f"{featured}{self.title}"