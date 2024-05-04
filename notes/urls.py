from django.urls import path

from .views import (
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    NoteListView,
    NoteCreateView,
    NoteUpdateView,
    NoteDeleteView,
    AuthorDetailView,
    archive_note,
    unarchive_note,
)

urlpatterns = [
    path(
        "category/",
        CategoryListView.as_view(),
        name="category-list",
    ),
    path(
        "category/create/",
        CategoryCreateView.as_view(),
        name="category-create",
    ),
    path(
        "category/<int:pk>/update/",
        CategoryUpdateView.as_view(),
        name="category-update",
    ),
    path(
        "category/<int:pk>/delete/",
        CategoryDeleteView.as_view(),
        name="category-delete",
    ),
    path("", NoteListView.as_view(), name="note-list"),
    path("note/create/", NoteCreateView.as_view(), name="note-create"),
    path(
        "note/<int:pk>/update/", NoteUpdateView.as_view(), name="note-update"
    ),
    path(
        "note/<int:pk>/delete/", NoteDeleteView.as_view(), name="note-delete"
    ),
    path("author/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("note/<int:pk>/archive/", archive_note, name="archive_note"),
    path("note/<int:pk>/unarchive/", unarchive_note, name="unarchive_note"),
]

app_name = "notes"
