from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)


class StickyNote(models.Model):
    # The task calls for both a title and content field for a sticky note.
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=80, default='Note')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
