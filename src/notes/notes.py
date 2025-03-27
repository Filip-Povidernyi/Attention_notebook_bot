from src.utils.common import print_help
from .classes.note_book import Notebook
from src.utils.decorators import auto_save_on_error

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
        "add":      "Add a new note (add <name>)",
        "view":     "View a note (view <name>)",
        "search":   "Search for a notes (search <term>)",
        "edit":     "Edit a note (edit <name>)",
        "delete":   "Delete a note (delete <name>)",
        "add_tag": "Add a tag to a note",
        "remove_tag": "Remove a tag from a note",
        "view_tags": "View tags of a note",
        "help":     "Show this help",
        "back":     "Go back to the main menu"
    }

    print("\n\nYou are in Notes now")
    print_help(commands)
    list_notes(notebook)

    while True:
        cmd_input = input("\nEnter a command (or 'help' for available commands): ").strip()
        cmd_parts = cmd_input.split(maxsplit=1)
        cmd = cmd_parts[0].lower()
        param = cmd_parts[1] if len(cmd_parts) > 1 else None

        match cmd:
            case "add":
                add_note(notebook, param)
                list_notes(notebook)
            case "view":
                view_note(notebook, param)
            case "search":
                search_notes(notebook, param)
            case "edit":
                edit_note(notebook, param)
                list_notes(notebook)
            case "delete":
                delete_note(notebook, param)
                list_notes(notebook)
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


def add_note(notebook: Notebook, name):
    if(not name):
        name = input("Enter note name: ").strip()
        
    content = input("Enter note content: ")
    note = notebook.add_note(name, content)
    if note:
        print(f"Note '{name}' added successfully.")
    else:
        print(f"Note '{name}' already exists.")

def view_note(notebook: Notebook, name):
    if(not name):
        name = input("Enter note name: ").strip()

    note = notebook.get_note(name)
    if note:
        print(note)
    else:
        print(f"Note '{name}' not found.")

def search_notes(notebook: Notebook, term):
    if(not term):
        term = input("Enter search term: ").strip()

    notes = notebook.search_notes(term)
    print(f"Found {len(notes)} notes matching the term '{term}'.")
    for note in notes:
        print(note)

def edit_note(notebook: Notebook, name):
    if(not name):
        name = input("Enter note name: ").strip()
    
    content = input("Enter new note content: ")
    note = notebook.edit_note(name, content)
    if note:
        print(f"Note '{name}' updated successfully.")
    else:
        print(f"Note '{name}' not found.")

def delete_note(notebook: Notebook, name):
    if(not name):
        name = input("Enter note name: ").strip()
    
    success = notebook.delete_note(name)
    if success:
        print(f"Note '{name}' deleted successfully.")
    else:
        print(f"Note '{name}' not found.")

def list_notes(notebook: Notebook):
    # TODO: pagination
    for note in notebook.notes:
        print(note)
