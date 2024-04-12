from django.urls import path
from .views import (
    send_content,
    read_content,
    read_note,
    delete_content,
    update_content,
    index,
)

urlpatterns = [
    path("", index, name="notes"),
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
