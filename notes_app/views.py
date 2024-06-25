from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404, render, redirect
from .models import StickyNote, Post
from .forms import NoteForm, PostForm, RegisterForm


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
            note.updated_at = timezone.now()
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


def register_view(request):
    """
    A new user registration page.
    """
    if request.method == 'POST':
        # Information was submitted: attempt to create a new user.
        # If successful, redirect to the login page.
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            # Ensure the password is saved as a hashed value.
            user.updated_at = timezone.now()
            form.save()
            return redirect('/accounts/login')
    else:
        # Landed on the page.
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)
