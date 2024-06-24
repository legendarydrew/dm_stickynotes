from django import forms
from .models import StickyNote, Post


class NoteForm(forms.ModelForm):
    """
    This sets up a form for creating or updating a StickyNote.
    """
    class Meta:
        model = StickyNote
        fields = ['title', 'content']


class PostForm(forms.ModelForm):
    """
    This sets up a form for creating or updating a Post.
    """

    class Meta:
        model = Post
        fields = ['title', 'content']
