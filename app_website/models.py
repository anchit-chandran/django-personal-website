import re

from django.db import models
from django.utils import timezone

# Create your models here.

class BlogPost(models.Model):

    posted_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    title = models.CharField(max_length=100, blank=False, null=True)
    header_img = models.URLField(max_length=2000, default='https://images.unsplash.com/photo-1559291001-693fb9166cba?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80')
    content = models.TextField(max_length=10000, blank=False, null=True)
    featured = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    
    def calculate_reading_time(self, reading_speed:int=200)->int:
        """Calculates reading time
        
        Returns -1 if no content.
        """
        
        if not self.content:
            return -1.0
        
        # Remove any non-word characters (e.g., punctuation)
        cleaned_text = re.sub(r'[^\w\s]', '', self.content)

        # Split the text into words
        words = cleaned_text.split()

        # Calculate the estimated reading time in minutes
        estimated_time = len(words) / reading_speed
        
        if estimated_time < 1:
            return 1

        # Return the estimated reading time rounded to the nearest whole number
        return round(estimated_time)
    
    def __str__(self):
        featured = "*" if self.featured else ""
        return f"{featured}Post {self.title}"


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

class Subscriber(models.Model):
    
    email = models.CharField(max_length=500, null=False, blank=False)
    name = models.CharField(max_length=500, null=False, blank=False)
    subscribed = models.BooleanField(default=False)
    
    confirmation_email_sent = models.BooleanField(default=False)
    
    def __str__(self):
        
        return f"{self.name}"