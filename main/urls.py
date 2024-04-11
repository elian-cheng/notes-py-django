from django.urls import path
from .views import (
    send_content,
    read_content,
    read_note,
    delete_content,
    update_content,
    special_page,
)

urlpatterns = [
    path(
        "",
        special_page,
    ),
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
