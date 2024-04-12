from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm


# Create your views here.
def index(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "notes.html")


def your_view_function(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        print(title, content)
        return redirect("notes")

    return render(request, "notes.html")


def send_content(request):
    # Retrieving all notes from the database
    new_note = Note(
        title="First Note", content="This is a first note", author="John Doe"
    )
    new_note.save()
    return HttpResponse("Note saved successfully")


def read_content(request):
    # Retrieving all notes from the database
    all_notes = Note.objects.all()
    return HttpResponse(all_notes)


def read_note(request):
    # Retrieving all notes from the database
    note = Note.objects.filter(title="New Note").first()
    return HttpResponse(note)


def delete_content(request):
    all_notes = Note.objects.all()
    for i in all_notes:
        i.delete()
    return HttpResponse("Notes deleted")


def update_content(request):
    all_notes = Note.objects.all()
    for note in all_notes:
        note.title = "LOL"
        note.save()
    return HttpResponse("Notes updated")
