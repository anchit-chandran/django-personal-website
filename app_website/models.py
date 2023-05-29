from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class BlogPost(models.Model):

    posted_at = models.DateTimeField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100, null=True)
    header_img = models.URLField(max_length=500, default=None, null=True)
    content = models.TextField(max_length=10000, null=True)
    featured = models.BooleanField(null=True)
    
    def __str__(self):
        featured = "*" if self.featured else ""
        return f"{featured}Post {self.title} by {self.author}"