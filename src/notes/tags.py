from .classes.note_book import Notebook

def search_notes_by_tag(notebook: Notebook, tag: str):
    found_notes = [note for note in notebook.notes if tag in note.tags]
    
    if found_notes:
        print(f"\nNotes with tag '{tag}':")
        for note in found_notes:
            print(f"- {note.name}: {note.content[:30]}...")
    else:
        print(f"\nNo notes found with tag '{tag}'.")

    return found_notes


def sort_notes_by_tags(notebook: Notebook):
    sorted_notes = sorted(notebook.notes, key=lambda note: len(note.tags), reverse=True)

    print("\nNotes sorted by number of tags:")
    for note in sorted_notes:
        print(f"- {note.name} ({len(note.tags)} tags)")

    return sorted_notes
