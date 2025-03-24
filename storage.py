import pickle
# from ... import AddressBook    #імпорти наших класів
# from ... import Note


FILENAMES = {
    "addressbook": "addressbook.pkl",
    "notes": "notes.pkl"
}

def load_data():
    try:
        with open(FILENAMES["addressbook"], "rb") as f:
            book = pickle.load(f)
    except (FileNotFoundError, EOFError):
        book = AddressBook()

    try:
        with open(FILENAMES["notes"], "rb") as f:
            notes = pickle.load(f)
    except (FileNotFoundError, EOFError):
        notes = Note()

    return book, notes

def save_data():
    with open(FILENAMES["addressbook"], "wb") as f:
        pickle.dump(book, f)
    with open(FILENAMES["notes"], "wb") as f:
        pickle.dump(notes, f)    #book, note будуть глобальними змінними у нашому основному файлі main.py