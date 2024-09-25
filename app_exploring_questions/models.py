from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    # id
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=10, blank=True, null=True)


class Article(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='articles')
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
