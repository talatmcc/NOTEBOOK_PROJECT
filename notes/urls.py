from django.urls import path, include
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.notes, name='notes'),
    path('note/<int:note_id>', views.note, name='note'),
    # path('edit/<int:note_id>', views.edit, name='edit'),
]
