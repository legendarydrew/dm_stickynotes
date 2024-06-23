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
