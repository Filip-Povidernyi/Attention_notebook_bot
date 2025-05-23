from src.utils.common import print_help
from .classes.note_book import Notebook
from src.utils.decorators import auto_save_on_error
from .tags import add_tag_to_note, remove_tag_from_note, view_tags_of_note, search_notes_by_tag, sort_notes_by_tags
from rich.console import Console
from rich.table import Table
from rich.box import ROUNDED
from rich.text import Text
from src.notes.node_editor import NoteEditor
from src.utils.autocomplete import suggest_command
from src.notes.utils.print_note import print_note_table
from src.utils.constants import MAIN_MENU_COMMANDS, NOTE_MENU_COMMANDS


"""
Module for managing notes in the application.

This module provides functionality to interact with and manage notes.
It includes a command-line interface (CLI) for performing actions such as 
displaying test messages and exiting the program.
"""

console = Console()


@auto_save_on_error
def notes_main(notebook: Notebook):
    """
    Main loop for managing notes in the application.

    This function presents a simple interface to the user for interacting with the notes section 
    of the application. It provides options for displaying a test message and exiting the program.
    """

    console.print("\n\nYou are in Notes now", style="steel_blue")
    print_help(NOTE_MENU_COMMANDS)
    list_notes(notebook)

    while True:

        cmd_input = None
        while not cmd_input:
            cmd_input = ask_command()

            if not cmd_input:
                console.print("Please enter a command from the list of available commands.", 
                            style="deep_pink4")
                continue

        cmd_parts = cmd_input.split(maxsplit=1)
        cmd = cmd_parts[0].lower()
        param = cmd_parts[1] if len(cmd_parts) > 1 else None

        match cmd:
            case "add" | "1":
                add_note(notebook, param)
                list_notes(notebook)

            case "view" | "2":
                view_note(notebook, param)

            case "search" | "3":
                search_notes(notebook, param)

            case "edit" | "4":
                edit_note(notebook, param)
                list_notes(notebook)

            case "delete" | "5":
                delete_note(notebook, param)
                list_notes(notebook)

            case "add_tag" | "6":
                handle_add_tag(notebook)

            case "remove_tag" | "7":
                handle_remove_tag(notebook)

            case "view_tags" | "8":
                handle_view_tags(notebook)

            case "search_tag" | "9":
                handle_search_tag(notebook)

            case "sort_by_tags" | "10":
                handle_sort_by_tags(notebook)

            case "help" | "11":
                print_help(NOTE_MENU_COMMANDS)

            case "back" | "0":
                print("\nGoing back to the main menu...")
                print_help(MAIN_MENU_COMMANDS)
                break
            case _:

                if not cmd:
                    console.print("Please enter a command from the list of available commands.", 
                                style="deep_pink4")
                    continue
                # Handle unknown commands
                suggested = suggest_command(
                    cmd, list(NOTE_MENU_COMMANDS.keys()), 0.5)
                if suggested:
                    print(
                        f"Unknown command '{cmd}'.\nMaybe you mean '{suggested}'?")

                else:
                    print(f"Unknown command '{cmd}'. Please try again.")


def ask_command():
    return input("\nEnter a command (or 'help' (11) for available commands): ").strip()


def add_note(notebook: Notebook, name):
    while not name:
        name = input("Enter note name: ").strip()

    if (notebook.get_note_by_name(name)):
        console.print(f"Note '{name}' already exists.", style="yellow")
        return

    editor = NoteEditor(name)
    editor.run()

    notebook.add_note(name, editor.saved_content)
    console.print(f"Note '{name}' added successfully!", style="green")


def view_note(notebook: Notebook, name):

    while not name:
        name = input("Enter note name: ").strip()

    note = notebook.get_note_by_name(name)
    if note:
        print_note_table(note)
    else:
        console.print(f"Note '{name}' not found.", style="red")


def search_notes(notebook: Notebook, term):

    while not term:
        term = input("Enter search term: ").strip()

    notes = notebook.search_notes(term)
    console.print(
        f"\nFound {len(notes)} notes matching the term '{term}'.", style="bold blue")
    for note in notes:
        print_note_table(note)


def edit_note(notebook: Notebook, name):
    while not name:
        name = input("Enter note name: ").strip()

    note = notebook.get_note_by_name(name)

    if not note:
        console.print(f"Note '{name}' not found.", style="red")
        return

    editor = NoteEditor(name, note.content)
    editor.run()

    if editor.saved_content is not None:
        notebook.edit_note(note.id, editor.saved_content)
        console.print(f"Note '{name}' updated successfully!", style="green")
    else:
        console.print(f"Note '{name}' edit cancelled.", style="yellow")


def delete_note(notebook: Notebook, name):
    while not name:
        name = input("Enter note name: ").strip()

    note = notebook.get_note_by_name(name)
    if not note:
        console.print(f"Note '{name}' not found.", style="yellow")
        return

    success = notebook.delete_note(note.id)
    if success:
        console.print(f"Note '{name}' deleted successfully.", style="green")
    else:
        console.print(f"Note '{name}' not found.", style="yellow")


def list_notes(notebook: Notebook):
    # TODO: pagination
    if not notebook.notes:
        console.print("No notes found.", style="yellow")
        return

    console.print(f"\nYour Notes: ({len(notebook.notes)})", style="bold blue")
    for note in notebook.notes:
        print_note_table(note)


def handle_add_tag(notebook: Notebook):
    note_name = input("Enter note name: ").strip()
    tag = input("Enter tag to add: ").strip()
    if add_tag_to_note(notebook, note_name, tag):
        return f"Tag '{tag}' added."
    else:
        return "Tag not added."


def handle_remove_tag(notebook: Notebook):
    note_name = input("Enter note name: ").strip()
    tag = input("Enter tag to remove: ").strip()
    if remove_tag_from_note(notebook, note_name, tag):
        return f"Tag '{tag}' removed."
    else:
        return "Tag not removed (may not exist)."


def handle_view_tags(notebook: Notebook):
    note_name = input("Enter note name: ").strip()
    tags = view_tags_of_note(notebook, note_name)
    if not tags:
        console.print("No tags found for this note.", style="yellow")
        return

    title_text = Text(f"Tags for Note: {note_name}", style="bold blue", overflow="fold")  
    table = Table(title=title_text, box=ROUNDED, show_header=True, min_width=35)
    table.add_column("Tags", style="bold")
    for tag in tags:
        table.add_row(tag)
    console = Console()
    console.print(table)

def handle_search_tag(notebook: Notebook):
    tag = input("Enter tag to search: ").strip()
    notes = search_notes_by_tag(notebook, tag)
    if not notes:
        console.print(f"No notes found with tag: {tag}", style="yellow")
        return
    console.print(f"\nNotes with tag '{tag}':", style="bold blue")
    for note in notes:
        print_note_table(note)

def handle_sort_by_tags(notebook: Notebook):
    sorted_notes = sort_notes_by_tags(notebook)
    if not sorted_notes:
        console.print("No notes found.", style="yellow")
        return
    console.print("\nSorted Notes:", style="bold blue")
    for note in sorted_notes:
        print_note_table(note)
