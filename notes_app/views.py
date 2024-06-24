import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import StickyNote, Post
from .forms import NoteForm, PostForm


'''
I'm using the Post model from the posts app.
https://stackoverflow.com/a/67601280/4073160
'''


# Create your views here.

@login_required
def home_view(request):
    """
    The main page, displaying the logged-in user's notes and posts from the posts app.
    If there is no logged-in user, we are redirected to the login page.
    """
    user = request.user
    context = {
        'username': user.username,
        'notes': StickyNote.objects.filter(owner=user),
        'posts': Post.objects.all(),
    }
    return render(request, 'home.html', context)


@login_required
def create_note_view(request):
    """
    Used when the user creates a note.
    """
    if request.method == 'POST':
        # The user submitted the form for creating a note.
        # If the data is valid, the note is created and the user sent
        # to the home page.
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            return redirect('home')
    else:
        # The user has landed on the page.
        form = NoteForm()
    return render(request, 'create_note.html', {'form': form})


@login_required
def create_post_view(request):
    """
    Used when the user creates a post.
    """
    if request.method == 'POST':
        """
        Create a new post, automatically setting the logged-in user
        as the author.
        """
        form = PostForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('home')
    else:
        # The user has landed on the page.
        form = PostForm()
    return render(request, 'create_Post.html', {'form': form})


@login_required
def update_note_view(request, note_id):
    """
    Used when the user updates a note.
    Users should only be able to update their own notes.
    """
    note = get_object_or_404(StickyNote, pk=note_id, owner=request.user)
    if request.method == 'POST':
        # The user submitted the form for updating the note.
        # If the data is valid, the note is updated and the user sent
        # to the home page.
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.updated_at = datetime.datetime.now()
            note.save()
            return redirect('home')
    else:
        # The user has landed on the page.
        form = NoteForm(instance=note)
    return render(request, 'update_note.html', {'form': form})


@login_required
def delete_note_view(request, note_id):
    """
    Used when the user deletes a note.
    If successful, the user is redirected to the home page.
    """
    note = get_object_or_404(StickyNote, pk=note_id, owner=request.user)
    note.delete()
    return redirect('home')
