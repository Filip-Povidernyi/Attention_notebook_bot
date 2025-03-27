from src.utils.common import print_help
from .classes.note_book import Notebook
from ..utils.decorators import auto_save_on_error

"""
Module for managing notes in the application.

This module provides functionality to interact with and manage notes.
It includes a command-line interface (CLI) for performing actions such as 
displaying test messages and exiting the program.
"""


@auto_save_on_error
def notes_main(notebook: Notebook):
    """
    Main loop for managing notes in the application.

    This function presents a simple interface to the user for interacting with the notes section 
    of the application. It provides options for displaying a test message and exiting the program.
    """

    commands = {
        "add":      "Add a new note",
        "view":     "View a note",
        "search":   "Search for a notes",
        "edit":     "Edit a note",
        "delete":   "Delete a note",
        "add_tag": "Add a tag to a note",
        "remove_tag": "Remove a tag from a note",
        "view_tags": "View tags of a note",
        "help":     "Show this help",
        "back":     "Go back to the main menu"
    }

    print("\n\nYou are in Notes now")

    print_help(commands)
    listNotes(notebook)

    while True:
        cmd = input(
            "\nEnter a command (or 'help' for available commands): ").strip().lower()

        match cmd:
            case "add":
                addNote(notebook)
                listNotes(notebook)
            case "view":
                viewNote(notebook)
            case "search":
                searchNotes(notebook)
            case "edit":
                editNote(notebook)
                listNotes(notebook)
            case "delete":
                deleteNote(notebook)
                listNotes(notebook)
            case "add_tag":
                note_name = input("Enter note name: ").strip()
                tag = input("Enter tag to add: ").strip()
                notebook.add_tag_to_note(note_name, tag)
            case "remove_tag":
                note_name = input("Enter note name: ").strip()
                tag = input("Enter tag to remove: ").strip()
                notebook.remove_tag_from_note(note_name, tag)
            case "view_tags":
                note_name = input("Enter note name: ").strip()
                notebook.view_tags_of_note(note_name)
            case "help":
                print_help(commands)
            case "back":
                print("\nYou are back to the main menu.")
                print_help({"1":    "Go to Address Book",
                            "2":    "Go to your Notes",
                            "help": "Show this help",
                            "exit": "Exit the application"})
                break
            case _:
                print("Unknown command. Please try again.")


def addNote(notebook: Notebook):
    name = input("Enter note name: ").strip()
    content = input("Enter note content: ")
    note = notebook.addNote(name, content)
    if note:
        print(f"Note '{name}' added successfully.")
    else:
        print(f"Note '{name}' already exists.")


def viewNote(notebook: Notebook):
    name = input("Enter note name: ").strip()
    note = notebook.getNote(name)
    if note:
        print(note)
    else:
        print(f"Note '{name}' not found.")


def searchNotes(notebook: Notebook):
    term = input("Enter search term: ").strip()
    notes = notebook.searchNotes(term)
    print(f"Found {len(notes)} notes matching the term '{term}'.")
    for note in notes:
        print(note)


def editNote(notebook: Notebook):
    name = input("Enter note name: ").strip()
    content = input("Enter new note content: ")
    note = notebook.editNote(name, content)
    if note:
        print(f"Note '{name}' updated successfully.")
    else:
        print(f"Note '{name}' not found.")


def deleteNote(notebook: Notebook):
    name = input("Enter note name: ").strip()
    success = notebook.deleteNote(name)
    if success:
        print(f"Note '{name}' deleted successfully.")
    else:
        print(f"Note '{name}' not found.")


def listNotes(notebook: Notebook):
    # TODO: pagination
    for note in notebook.notes:
        print(note)
