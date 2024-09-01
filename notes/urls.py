from django.urls import path, include
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.notes, name='notes'),
    path('new_note/', views.new_note, name='new_note'),
    path('note/<int:note_id>', views.note, name='note'),
    # path('edit/<int:note_id>', views.edit, name='edit'),
]
