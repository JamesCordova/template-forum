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

class PostBase(Base):
    content = MarkdownxField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    votes = models.IntegerField(default=0)
    
    class Meta:
        abstract = True;
        ordering = ['votes', '-created_at']
    
class Post(PostBase):
    title = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default=0)
    tags = models.ManyToManyField(Tag)
    
    class Meta:
        ordering = ['votes', '-created_at']

class SubPost(PostBase):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['votes', '-created_at']

class Response(Base):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subpost = models.ForeignKey(SubPost, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BookMark(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bookmarks = models.ManyToManyField(Post)
    