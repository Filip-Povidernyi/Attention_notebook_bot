import os
from src.contacts_fold.classes.contacts_book import ContactsBook
from src.notes.classes.note_book import Notebook
import pickle
# import pyzipper   #Стороння бібліотека, яку використав для архівування
# import os
# from ... import Note


FILENAMES = {
    "addressbook": "db/addressbook.pkl",
    "notes": "db/notes.pkl"
}


def load_data():
    try:
        with open(FILENAMES["addressbook"], "rb") as f:
            book = pickle.load(f)
    except (FileNotFoundError, EOFError):
        book = ContactsBook()

    try:
        with open(FILENAMES["notes"], "rb") as f:
            notes = pickle.load(f)
    except (FileNotFoundError, EOFError):
        notes = Notebook()

    return book, notes


def save_data(book, notes):
    os.makedirs(os.path.dirname(FILENAMES["addressbook"]), exist_ok=True)
    with open(FILENAMES["addressbook"], "wb") as f:
        pickle.dump(book, f)
    os.makedirs(os.path.dirname(FILENAMES["notes"]), exist_ok=True)
    with open(FILENAMES["notes"], "wb") as f:
        pickle.dump(notes, f)


# Варіант із архівуванням під паролем:

# ARCHIVE_FILE = "data.zip"

# PASSWORD = input("Enter password: ").encode()

# def save_data(book, notes):
#     temp_files = []

#     book_file = FILENAMES["addressbook"]
#     with open(book_file, "wb") as f:
#         pickle.dump(book, f)
#     temp_files.append(book_file)


#     notes_file = FILENAMES["notes"]
#     with open(notes_file, "wb") as f:
#         pickle.dump(notes, f)
#     temp_files.append(notes_file)

#     with pyzipper.AESZipFile(ARCHIVE_FILE, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zf:   # Це саме створення ZIP-архів із шифруванням
#         zf.setpassword(PASSWORD)
#         for file in temp_files:
#             zf.write(file)
#             os.remove(file)

# def load_data():
#     if not os.path.exists(ARCHIVE_FILE):
#         return {}, {}

#     with pyzipper.AESZipFile(ARCHIVE_FILE, 'r') as zf:
#         try:
#             zf.setpassword(PASSWORD)

#             with zf.open(FILENAMES["addressbook"]) as f:
#                 book = pickle.load(f)

#             with zf.open(FILENAMES["notes"]) as f:
#                 notes = pickle.load(f)

#         except RuntimeError:
#             print("❌ Неправильний пароль! Дані не можуть бути завантажені.")
#             return None, None

#     return book, notes
