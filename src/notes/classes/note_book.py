from typing_extensions import deprecated
from .note import Note


class Notebook:
    def __init__(self):
        self.max_id = 0
        self.notes: list[Note] = []

    def add_note(self, name: str, content: str):
        # TODO: check if note already exists
        note = Note(name, id=self._get_next_id())
        note.set_content(content)
        self.notes.append(note)
        self._sort_notes()
        
        return note
    
    def get_note(self, id: int) -> Note | None:
        return next((x for x in self.notes if x.id == id), None)
    
    @deprecated("Use get_note instead as name is not unique")
    def get_note_by_name(self, name: str) -> Note | None:
        return next((x for x in self.notes if x.name == name), None)

    def edit_note(self, id: int, content: str) -> Note | None:
        note = self.get_note(id)
        if not note:
            return None
        
        note.set_content(content)
        self._sort_notes()
        
        return note

    def search_notes(self, term: str) -> list[Note]:
        return [x for x in self.notes if self._search_condition(term, x)]

    def delete_note(self, id: int) -> bool:
        notes = [x for x in self.notes if x.id != id]
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
    
    def _get_next_id(self):
        self.max_id += 1
        return self.max_id

    def __setstate__(self, state):
        """Called by pickle after deserialization.
        
        This method is used to handle data migrations and hydration.
        """
        
        self.__dict__.update(state)
        
        max_id = 0
        for note in self.notes:
            if hasattr(note, 'id') and note.id > max_id:
                max_id = note.id
                
        self.max_id = max_id
                
        for note in self.notes:
            if not hasattr(note, 'id') or note.id is None:
                note.id = self._get_next_id()

