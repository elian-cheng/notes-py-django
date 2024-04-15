from django.urls import path
from .views import (
    send_content,
    read_content,
    read_note,
    delete_content,
    update_content,
    index,
    note_detail,
    delete,
)

urlpatterns = [
    path("", index, name="notes"),
    path("note/<int:note_id>/", note_detail, name="note_detail"),
    path("note/<int:note_id>/delete/", delete, name="delete"),
    path(
        "read/",
        read_content,
    ),
    path(
        "send/",
        send_content,
    ),
    path(
        "record/",
        read_note,
    ),
    path("update/", update_content),
    path("delete/", delete_content),
]
