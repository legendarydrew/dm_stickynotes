from django.urls import path
from .views import home_view, create_post_view, create_note_view, update_note_view, delete_note_view

urlpatterns = [
    path('', home_view, name='home'),
    path('create', create_note_view, name='create_note'),
    path('post', create_post_view, name='create_post'),
    path('update/<int:note_id>', update_note_view, name='update_note'),
    path('delete/<int:note_id>', delete_note_view, name='delete_note')
]
