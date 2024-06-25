from django import forms
from django.contrib.auth.models import User
from .models import StickyNote, Post


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


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
