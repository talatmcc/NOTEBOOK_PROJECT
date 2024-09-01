from django.shortcuts import render
from .models import Note, Entry

# Create your views here.

# myNotes = [
#     {
#         "id": 1,
#         "title": "First Note",
#         "Entries": ["This is the 1.1 note", "This is the 1.2 note", "This is the 1.3 note"],    
#     },
#     {
#         "id": 2,
#         "title": "Second Note",
#         "Entries": ["This is the 2.1 note", "This is the 2.2 note", "This is the 2.3 note"],
#     },
#     {
#         "id": 3,
#         "title": "Third Note",
#         "Entries": ["This is the 3.1 note", "This is the 3.2 note", "This is the 3.3 note"],
#     },
# ]


def home(request):
    return render(request, "notes/home.html")


def notes(request):
    notes = Note.objects.order_by("date_added")
    context = {"notes": notes}
    return render(request, "notes/notes.html", context)

def note(request, note_id):
    note = Note.objects.get(id=note_id)
    entries = note.entry_set.order_by("date_added")
    context = {"note": note, 'entries': entries}
    return render(request, "notes/note.html", context)

# def edit(request, note_id):
#     for myNote in myNotes:
#         if myNote["id"] == note_id:
#             note = myNote

#     context = {"note": note, 'entries': note["Entries"]}
#     return render(request, "notes/edit.html", context)