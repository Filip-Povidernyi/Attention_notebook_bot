
from .note import Note


class Notebook:
    def __init__(self):
        self.notes: list[Note] = []

    def addNote(self, name: str, content: str):
        # TODO: check if note already exists
        note = Note(name)
        note.setContent(content)
        self.notes.append(note)
        self._sortNotes()
        
        return note
    
    def getNote(self, name: str) -> Note | None:
        return next((x for x in self.notes if x.name == name), None)

    def editNote(self, name: str, content: str) -> Note | None:
        note = self.getNote(name)
        if not note:
            return None
        
        note.setContent(content)
        self._sortNotes()
        
        return note

    def searchNotes(self, term: str) -> list[Note]:
        return [x for x in self.notes if self._searchCondition(term, x)]

    def deleteNote(self, name: str) -> bool:
        notes = [x for x in self.notes if x.name != name]
        if len(notes) == len(self.notes):
            return False
        
        self.notes = notes
        return True
    
    def _searchCondition(self, term: str, note: Note) -> bool:
        return term in note.name or term in note.content
    
    def _sortNotes(self):
        self.notes.sort(key=lambda x: x.updatedAt, reverse=True)
            
    def __str__(self):
        return "\n".join([f"{note['name']}: {note['content']}" for note in self.notes])

    def __repr__(self):
        return f"Notebook({self.notes})"

