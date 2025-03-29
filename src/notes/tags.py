from .classes.note_book import Notebook

def add_tag_to_note(notebook: Notebook, note_name: str, tag: str) -> bool:
    note = notebook.get_note(note_name)
    if not note:
        return False
    return note.add_tag(tag)

def remove_tag_from_note(notebook: Notebook, note_name: str, tag: str) -> bool:
    note = notebook.get_note(note_name)
    if not note:
        return False
    return note.remove_tag(tag)

def view_tags_of_note(notebook: Notebook, note_name: str) -> list[str]:
    note = notebook.get_note(note_name)
    if not note:
        return []
    return note.view_tags()

def search_notes_by_tag(notebook: Notebook, tag: str) -> list:
    tag_lower = tag.lower()
    return [
        note for note in notebook.notes
        if tag_lower in (t.lower() for t in note.tags)
    ]

def sort_notes_by_tags(notebook: Notebook):
    return sorted(notebook.notes, key=lambda note: len(note.tags), reverse=True)
