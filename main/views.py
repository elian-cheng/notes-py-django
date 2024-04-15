from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm


# Create your views here.
# this line fetches all objects from the Note model in the database and sorts them
# by the id field in descending order. The result is stored in the variable notes and
# can be used, for example, to pass to a template for displaying a list of records.
# {'notes': notes}: This is a Python dictionary that passes data to be used in the template.
# In the template, you can access this data using the key "notes".
def index(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()

    notes = Note.objects.all().order_by("-id")
    return render(request, "notes.html", {"notes": notes})


# .get(pk=note_id): This get method is used to retrieve a single object from the database
# that matches certain criteria. In this case, the criteria is the
# identifier of the record (pk=note_id), which is passed as the note_id parameter.
def note_detail(request, note_id):
    note = Note.objects.get(pk=note_id)

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            note.title = title
            note.content = content
            note.save()
            return redirect("notes")

    return render(request, "note_detail.html", {"note": note})


def delete(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.delete()

    notes = Note.objects.all().order_by("-id")
    render(request, "notes.html", {"notes": notes})
    return redirect("/")


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
