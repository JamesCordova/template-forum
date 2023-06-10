from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField

class Base(models.Model):
    STATE_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
        ('X', 'Deleted'),
    )
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default='A')

    class Meta:
        abstract = True
class Tag(models.Model):
    name = models.CharField(max_length=255)

class Topic(Base):
    name = models.CharField(max_length=255)

class Post(Base):
    title = models.CharField(max_length=255)
    content = MarkdownxField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default=0)
    tags = models.ManyToManyField(Tag)

class SubPost(Base):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Response(Base):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subpost = models.ForeignKey(SubPost, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
