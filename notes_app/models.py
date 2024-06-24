from django.db import models
from django.conf import settings


# Create your models here.


class StickyNote(models.Model):
    """
    The task calls for both a title and content field for a sticky note.
    When created the created_at and updated_at columns should be set to
    the current time.
    """
    title = models.CharField(max_length=80)
    content = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    """
    Model representing a bulletin board post.
    Fields:
    - title: CharField for the post title with a maximum length of 255
    characters.
    - content: TextField for the post content.
    - created_at: DateTimeField set to the current date and time when the
    post is created.
    Relationships:
    - author: ForeignKey representing the author of the post.
    Methods:
    - No specific methods are defined in this model.
    :param models.Model: Django's base model class.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Define a ForeignKey for the author's relationship
    # Changing the author relationship to use the User table.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
