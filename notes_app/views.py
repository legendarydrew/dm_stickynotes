import datetime
from django.shortcuts import get_object_or_404, render, redirect
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
            note = form.save()
            # note = form.save(commit=False)
            # note.save()
            return redirect('home')
    else:
        form = NoteForm()    
    return render(request, 'create_note.html', { 'form': form })


def update_view(request, note_id):
    """
    Used when the user updates a note.
    """
    note = get_object_or_404(StickyNote, pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.updated_at = datetime.datetime.now()
            note.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)
    return render(request, 'update_note.html', {'form': form})


def delete_view(request, note_id):
    """
    Used when the user deletes a note.
    """
    note = get_object_or_404(StickyNote, pk=note_id)
    note.delete()
    return redirect('home')
