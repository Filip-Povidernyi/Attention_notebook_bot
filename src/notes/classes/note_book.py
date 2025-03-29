from .note import Note


class Notebook:
    def __init__(self):
        self.notes: list[Note] = []

    def add_note(self, name: str, content: str):
        # TODO: check if note already exists
        note = Note(name)
        note.set_content(content)
        self.notes.append(note)
        self._sort_notes()
        
        return note
    
    def get_note(self, name: str) -> Note | None:
        return next((x for x in self.notes if x.name == name), None)

    def edit_note(self, name: str, content: str) -> Note | None:
        note = self.get_note(name)
        if not note:
            return None
        
        note.set_content(content)
        self._sort_notes()
        
        return note

    def search_notes(self, term: str) -> list[Note]:
        return [x for x in self.notes if self._search_condition(term, x)]

    def delete_note(self, name: str) -> bool:
        notes = [x for x in self.notes if x.name != name]
        if len(notes) == len(self.notes):
            return False
        
        self.notes = notes
        return True
    
    def _search_condition(self, term: str, note: Note) -> bool:
        return term in note.name or term in note.content
    
    def _sort_notes(self):
        self.notes.sort(key=lambda x: x.updated_at, reverse=True)
            
    def __str__(self):
        return "\n".join([f"{note['name']}: {note['content']}" for note in self.notes])

    def __repr__(self):
        return f"Notebook({self.notes})"

