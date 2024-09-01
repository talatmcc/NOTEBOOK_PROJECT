from django import forms
from .models import Note, Entry

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title']
        labels = {'title': 'Title'}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        # labels = {'text': 'Entry:'}
        # widgets = {'text': forms.Textarea(attrs={'cols': 80})}

# The NoteForm class inherits from forms.ModelForm, which is a parent class included in Django that defines the functionality for creating forms from models.