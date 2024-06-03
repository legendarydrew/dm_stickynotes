from django.urls import path
from .views import home_view, create_view, update_view

urlpatterns = [
    path('', home_view, name='home'),
    path('create', create_view, name='create_note'),
    path('update/<int:note_id>', update_view, name='update_note'),
]
