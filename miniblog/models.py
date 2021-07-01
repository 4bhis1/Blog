from django.db import models

# Create your models here.

class Post_the_blog(models.Model):
    title=models.CharField(max_length=150)
    desc=models.TextField()