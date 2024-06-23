from django import forms
from .models import StickyNote


class NoteForm(forms.ModelForm):
    """
    This sets up a form for creating or updating a StickyNote.
    """
    class Meta:
        model = StickyNote
        fields = ['title', 'content']
