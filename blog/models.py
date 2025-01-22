from django.db import models

# Create your models here.

from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=400, help_text="Enter your bio details here.")
    
    class Meta:
        ordering = ["user","bio"]

    def get_absolute_url(self):
        return reverse('blog_by_user', args=[str(self.id)])

    def __str__(self):
        return self.user.username


class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=2000, help_text="What's on your mind?")
    upload_time = models.DateField(default=date.today)
    
    class Meta:
        ordering = ["-upload_time"]
    
    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])

    def __str__(self):
        return self.title
        
        
class Comment(models.Model):
    description = models.TextField(max_length=1000, help_text="Enter comment about blog here.")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    upload_time = models.DateTimeField(auto_now_add=True)
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["upload_time"]

    def __str__(self):
        len_title=75
        if len(self.description)>len_title:
            titlestring=self.description[:len_title] + '...'
        else:
            titlestring=self.description
        return titlestring




