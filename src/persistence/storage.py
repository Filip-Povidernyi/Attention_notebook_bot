import os
from ..contacts.classes.contacts_book import ContactsBook
from ..notes.classes.note_book import Notebook
import pickle
import pyzipper   
import os
from src.utils.password import prompt_password


FILENAMES = {
    "addressbook": "db/addressbook.pkl",
    "notes": "db/notes.pkl"
}

# Варіант без архівуванням та пароля:

# def load_data():
#     try:
#         with open(FILENAMES["addressbook"], "rb") as f:
#             book = pickle.load(f)
#     except (FileNotFoundError, EOFError):
#         book = ContactsBook()

#     try:
#         with open(FILENAMES["notes"], "rb") as f:
#             notes = pickle.load(f)
#     except (FileNotFoundError, EOFError):
#         notes = Notebook()

#     return book, notes


# def save_data(book, notes):
#     os.makedirs(os.path.dirname(FILENAMES["addressbook"]), exist_ok=True)
#     with open(FILENAMES["addressbook"], "wb") as f:
#         pickle.dump(book, f)
#     os.makedirs(os.path.dirname(FILENAMES["notes"]), exist_ok=True)
#     with open(FILENAMES["notes"], "wb") as f:
#         pickle.dump(notes, f)


# Варіант із архівуванням під паролем:

ARCHIVE_FILE = "data.zip"


def save_data(book, notes, PASSWORD):
    if not isinstance(book, ContactsBook):
        print("[ERROR] book is not an instance of ContactsBook.")
        return
    if not isinstance(notes, Notebook):
        print("[ERROR] notes is not an instance of Notebook.")
        return

    temp_files = []

    book_file = FILENAMES["addressbook"]
    with open(book_file, "wb") as f:
        pickle.dump(book, f)
    temp_files.append(book_file)


    notes_file = FILENAMES["notes"]
    with open(notes_file, "wb") as f:
        pickle.dump(notes, f)
    temp_files.append(notes_file)

    with pyzipper.AESZipFile(ARCHIVE_FILE, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zf:   # Це саме створення ZIP-архів із шифруванням
        zf.setpassword(PASSWORD)
        for file in temp_files:
            zf.write(file)
            os.remove(file)

def load_data(PASSWORD):
    if not os.path.exists(ARCHIVE_FILE):
        print("[ERROR] Archive file not found.")
        return ContactsBook(), Notebook()
    
    while True:
        try:
            with pyzipper.AESZipFile(ARCHIVE_FILE, 'r') as zf:
                zf.setpassword(PASSWORD)

                with zf.open(FILENAMES["addressbook"]) as f:
                    book = pickle.load(f)

                with zf.open(FILENAMES["notes"]) as f:
                    notes = pickle.load(f)

                if not isinstance(book, ContactsBook):
                    print("[ERROR] Loaded book is not an instance of ContactsBook.")
                    return None, None
                if not isinstance(notes, Notebook):
                    print("[ERROR] Loaded notes is not an instance of Notebook.")
                    return None, None

                return book, notes

        except RuntimeError:
            print("❌ Incorrect password! Try again.")
            return None, None
        except Exception as e:
            print(f"❌ An error occurred while loading data: {e}")
            return ContactsBook(), Notebook()
