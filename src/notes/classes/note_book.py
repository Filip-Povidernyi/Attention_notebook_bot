
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

    def add_tag_to_note(self, note_name: str, tag: str):
        note = self.getNote(note_name)
        if note:
            if note.add_tag(tag):
                print(f"Tag '{tag}' added to note '{note_name}'.")
            else:
                print(f"Tag '{tag}' already exists on note '{note_name}'.")
        else:
            print(f"Note '{note_name}' not found.")
    
    def remove_tag_from_note(self, note_name: str, tag: str):
        note = self.getNote(note_name)
        if note:
            if note.remove_tag(tag):
                print(f"Tag '{tag}' removed from note '{note_name}'.")
            else:
                print(f"Tag '{tag}' not found on note '{note_name}'.")
        else:
            print(f"Note '{note_name}' not found.")
    
    def view_tags_of_note(self, note_name: str):
        note = self.getNote(note_name)
        if note:
            tags = note.view_tags()
            if tags:
                print(f"Tags for '{note_name}': {', '.join(tags)}")
            else:
                print(f"No tags found for note '{note_name}'.")
        else:
            print(f"Note '{note_name}' not found.")
            
    def __str__(self):
        return "\n".join([f"{note['name']}: {note['content']}" for note in self.notes])

    def __repr__(self):
        return f"Notebook({self.notes})"

