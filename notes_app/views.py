from django.shortcuts import render, redirect
from .models import StickyNote 

# Create your views here.
def home_view(request):
    """
    The main page, displaying all of the user's notes.
    """

    notes = StickyNote.objects.all()

    context = {
        'notes': notes
    }

    return render(request, 'home.html', context)


def create_view(request):
    """
    Used when the user creates a note.
    """
    return redirect('home')


def update_view(request):
    """
    Used when the user updates a note.
    """
    return redirect('home')


def archive_view(request):
    """
    Used when the user archives a note.
    """
    return redirect('home')


def delete_view(request):
    """
    Used when the user deletes a note.
    """
    return redirect('home')
