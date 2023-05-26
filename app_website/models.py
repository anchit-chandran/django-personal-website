from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class BlogPost(models.Model):

    posted_at = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    header_img = models.URLField(max_length=500)
    content = models.TextField(max_length=2000)
    featured = models.BooleanField()
    
    def __str__(self):
        return f"Post {self.title} by {self.author}"