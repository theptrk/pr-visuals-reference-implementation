"""Catalog business logic — no schema impact."""

from django.db import transaction
from django.db.models import Q

from .models import Note
from .models import Tag


def search_notes(term):
    """Return notes whose title matches the term, most recent first."""
    return Note.objects.filter(title__icontains=term)


def merge_tags(primary: Tag, duplicate: Tag) -> int:
    """Move all notes from `duplicate` onto `primary`, then delete `duplicate`.

    Returns the number of note-tag links moved.
    """
    if primary.pk == duplicate.pk:
        raise ValueError("Cannot merge a tag into itself")
    with transaction.atomic():
        duplicate_links = duplicate.notes.all()
        moved = duplicate_links.filter(~Q(tags__pk=primary.pk)).count()
        for note in duplicate_links:
            note.tags.add(primary)
            note.tags.remove(duplicate)
        duplicate.delete()
    return moved
