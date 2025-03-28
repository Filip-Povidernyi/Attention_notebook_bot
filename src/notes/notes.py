from src.utils.common import print_help
from .classes.note_book import Notebook, Note
from src.utils.decorators import auto_save_on_error
from rich.console import Console
from src.notes.node_editor import NoteEditor
# from src.notes.list_view import ListView, ListItem, Label
from textual.app import App, ComposeResult, Screen
from textual.widgets import Footer, Label, ListItem, ListView
from textual.widgets import DataTable, Footer
from rich.text import Text

"""
Module for managing notes in the application.

This module provides functionality to interact with and manage notes.
It includes a command-line interface (CLI) for performing actions such as 
displaying test messages and exiting the program.
"""

console = Console()
list_view = ListView()



ROWS = [
    ("lane", "swimmer", "country", "time 1", "time 2"),
    (4, "Joseph Schooling", Text("Singapore", style="italic"), 50.39, 51.84),
    (2, "Michael Phelps", Text("United States", style="italic"), 50.39, 51.84),
    (5, "Chad le Clos", Text("South Africa", style="italic"), 51.14, 51.73),
    (6, "László Cseh", Text("Hungary", style="italic"), 51.14, 51.58),
    (3, "Li Zhuhao", Text("China", style="italic"), 51.26, 51.26),
    (8, "Mehdy Metella", Text("France", style="italic"), 51.58, 52.15),
    (7, "Tom Shields", Text("United States", style="italic"), 51.73, 51.12),
    (1, "Aleksandr Sadovnikov", Text("Russia", style="italic"), 51.84, 50.85),
    (10, "Darren Burns", Text("Scotland", style="italic"), 51.84, 51.55),
]

class ListViewExample(App):
    # CSS_PATH = "list_view.tcss"

    def compose(self) -> ComposeResult:
        yield ListView(
            ListItem(Label("One")),
            ListItem(Label("Two")),
            ListItem(Label("Three")),
        )
        yield Footer()


class NewScreen(Screen):
    """The new screen that will be displayed dynamically."""

    def __init__(self, name, content):
        super().__init__()
        self.x_name = name
        self.x_content = content

    def compose(self) -> ComposeResult:
        yield NoteEditor(self.x_name, self.x_content)

    def on_button_pressed(self, event) -> None:
        """Handle button press to go back."""
        if event.button.id == "back":
            self.app.pop_screen()


class TableApp(App):
    BINDINGS = [
        ("q", "quit", "Quit"),

        ("e", "edit", "Edit note")

        # ("a", "sort_by_average_time", "Sort By Average Time"),
        # ("n", "sort_by_last_name", "Sort By Last Name"),
        # ("c", "sort_by_country", "Sort By Country"),
        # ("d", "sort_by_columns", "Sort By Columns (Only)"),
    ]

    def __init__(self, notebook):
        super().__init__()
        self.notebook = notebook

    current_sorts: set = set()

    def action_quit(self):
        self.exit(0)


    def on_data_table_row_selected(self, e: DataTable.RowSelected):
        print(e)

    def on_data_table_row_highlighted(self, e: DataTable.RowHighlighted):
        print(e)
        self.selected_row = e.row_key

    def action_edit(self):
        table = self.query_one(DataTable)
        index = table.cursor_row


        if self.selected_row:
            name = self.selected_row
            notebook = self.notebook
            # edit_note(self.notebook, self.selected_row)

            note = notebook.get_note(name)

            if not note:
                console.print(f"Note '{name}' not found.", style="red")
                return
            
            # editor = NoteEditor(name, note.content)
            screen = NewScreen(name, note.content)
            self.push_screen(screen)


    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = "row"
        self.list(self.notebook.notes)

    def list(self, notes):
        table = self.query_one(DataTable)
        table.clear()
        for col in ["name", "updated_at", "content"]:
            table.add_column(col, key=col)

        ns = map(lambda n: (n.name, n.updated_at, n.content[:20]), notes)

        for n in notes:
            table.add_row((n.name, n.updated_at, n.content[:20]), key=n.name, label=n.name + "KEY")

        # table.add_rows(ns)

    def sort_reverse(self, sort_type: str):
        """Determine if `sort_type` is ascending or descending."""
        reverse = sort_type in self.current_sorts
        if reverse:
            self.current_sorts.remove(sort_type)
        else:
            self.current_sorts.add(sort_type)
        return reverse

    def action_sort_by_average_time(self) -> None:
        """Sort DataTable by average of times (via a function) and
        passing of column data through positional arguments."""

        def sort_by_average_time_then_last_name(row_data):
            name, *scores = row_data
            return (sum(scores) / len(scores), name.split()[-1])

        table = self.query_one(DataTable)
        table.sort(
            "swimmer",
            "time 1",
            "time 2",
            key=sort_by_average_time_then_last_name,
            reverse=self.sort_reverse("time"),
        )

    def action_sort_by_last_name(self) -> None:
        """Sort DataTable by last name of swimmer (via a lambda)."""
        table = self.query_one(DataTable)
        table.sort(
            "swimmer",
            key=lambda swimmer: swimmer.split()[-1],
            reverse=self.sort_reverse("swimmer"),
        )

    def action_sort_by_country(self) -> None:
        """Sort DataTable by country which is a `Rich.Text` object."""
        table = self.query_one(DataTable)
        table.sort(
            "country",
            key=lambda country: country.plain,
            reverse=self.sort_reverse("country"),
        )

    def action_sort_by_columns(self) -> None:
        """Sort DataTable without a key."""
        table = self.query_one(DataTable)
        table.sort("swimmer", "lane", reverse=self.sort_reverse("columns"))




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
        "view_all":     "View all notes",
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

    for node in notebook.notes:
        console.print(node)
    

    # app = ListViewExample()
    app = TableApp(notebook)
    app.run()

    # app.list(notebook.notes)

    # list_notes(notebook)
    return

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
            case "view_all":
                list_notes(notebook)
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
    
    if(notebook.get_note(name)):
        console.print(f"Note '{name}' already exists.", style="yellow")
        return

    editor = NoteEditor(name)
    editor.run()

    notebook.add_note(name, editor.saved_content)
    console.print(f"Note '{name}' added successfully!", style="green")

def view_note(notebook: Notebook, name):
    if(not name):
        name = input("Enter note name: ").strip()

    note = notebook.get_note(name)
    if note:
        console.print(note)
    else:
        console.print(f"Note '{name}' not found.", style="red")

def search_notes(notebook: Notebook, term):
    if(not term):
        term = input("Enter search term: ").strip()

    notes = notebook.search_notes(term)
    console.print(f"\nFound {len(notes)} notes matching the term '{term}'.", style="bold blue")
    for note in notes:
        console.print("\n" + "─" * 50, style="dim")
        console.print(note)

def edit_note(notebook: Notebook, name):
    if(not name):
        name = input("Enter note name: ").strip()
    
    note = notebook.get_note(name)

    if not note:
        console.print(f"Note '{name}' not found.", style="red")
        return
    
    editor = NoteEditor(name, note.content)
    editor.run()

    if editor.saved_content is not None:
        notebook.edit_note(note.name, editor.saved_content)
        console.print(f"Note '{name}' updated successfully!", style="green")
    else:
        console.print(f"Note '{name}' edit cancelled.", style="yellow")


def delete_note(notebook: Notebook, name):
    if(not name):
        name = input("Enter note name: ").strip()
    
    success = notebook.delete_note(name)
    if success:
        print(f"Note '{name}' deleted successfully.")
    else:
        print(f"Note '{name}' not found.")

def list_notes(notebook: Notebook):
    """Display notes using ListView."""
    list_view.clear()
    if not notebook.notes:
        console.print("No notes found.", style="yellow")
        return
    
    for note in notebook.notes:
        item = ListItem(Label(f"{note.name}: {note.content}"))
        list_view.add(item)
    
    console.print(list_view)
