from django import forms
from .models import Note

# class Meta
# model = Note: Tells Django that this form is associated with the Note model;
# fields = ['title', 'content']: Specifies exactly which fields from the model we want to include in our form.


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content"]
