from django.db import models


# Create your models here.

class StickyNote(models.Model):
    # The task calls for both a title and content field for a sticky note.
    title = models.CharField(max_length=80, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
