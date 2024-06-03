from django.shortcuts import render, redirect
from .models import StickyNote 
from .forms import NoteForm

# Create your views here.
def home_view(request):
    """
    The main page, displaying all of the user's notes.
    """

    context = {
        'notes': StickyNote.objects.all()
    }

    return render(request, 'home.html', context)


def create_view(request):
    """
    Used when the user creates a note.
    """
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            # TODO add a reference to the authenticated user.
            note.save()
            return redirect('home')
    else:
        form = NoteForm()    
    return render(request, 'create_note.html', { 'form': form })

def update_view(request):
    """
    Used when the user updates a note.
    """
    return redirect('home')


def delete_view(request):
    """
    Used when the user deletes a note.
    """
    return redirect('home')
