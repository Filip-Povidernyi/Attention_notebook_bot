from typing import Callable
from src.utils.common import print_help
from .classes.note_book import Notebook, Note
from src.utils.decorators import auto_save_on_error
from rich.console import Console
from src.notes.node_editor_ui import NoteEditor, NoteEditorApp
from textual.app import App, ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Footer, Label, DataTable, Footer, Button, TextArea, Static, Input
from textual.containers import Grid, Container, Vertical
from textual.binding import Binding

"""
Module for managing notes in the application.

This module provides functionality to interact with and manage notes.
It includes a command-line interface (CLI) for performing actions such as 
displaying test messages and exiting the program.
"""

console = Console()

class EditorScreen(ModalScreen[str]):
    """The new screen that will be displayed dynamically."""
    
    BINDINGS = [
        Binding("ctrl+o", "save", "Save", show=True),
        Binding("escape,f10", "quit", "Quit", show=True),
    ]

    def __init__(self, name, content, editable: bool, on_close: Callable[[str, Callable[[bool], None]], None]):
        super().__init__()
        self.x_name = name
        self.x_content = content
        self.saved_content = None
        self.editable = editable
        self.on_close = on_close
        
    def compose(self) -> ComposeResult:
        yield NoteEditor(self.x_name, self.x_content, self.editable)
        
    def action_save(self) -> None:
        editor = self.query_one(NoteEditor)
        self.saved_content = editor.get_text()
        self.notify("Content saved!")

    def action_quit(self) -> None:
        editor = self.query_one(NoteEditor)
        if (self.x_content == editor.get_text()):
            self.dismiss(self.saved_content)
            return
        
        def on_close(result: bool):
            if result:
                self.dismiss(None)
            
        self.on_close("Unsaved changes, are you sure you want to quit?", on_close)

    def on_button_pressed(self, event) -> None:
        """Handle button press to go back."""
        if event.button.id == "back":
            self.app.pop_screen()

class AskScreen(ModalScreen[bool]):
    """Screen with a dialog to ask a question."""
    
    CSS = """
    AskScreen {
        align: center middle;
    }

    #dialog {
        grid-size: 2;
        grid-gutter: 1 2;
        grid-rows: 1fr 3;
        padding: 0 1;
        width: 40%;
        height: 11;
        border: thick $background 80%;
        background: $surface;
    }

    #question {
        column-span: 2;
        height: 1fr;
        width: 1fr;
        content-align: center middle;
    }

    Button {
        width: 100%;
    }
    """
    
    def __init__(self, question: str):
        super().__init__()
        self.question = question

    def compose(self) -> ComposeResult:
        yield Grid(
            Label(self.question, id="question"),
            Button("Yes", variant="error", id="yes"),
            Button("No", variant="primary", id="no"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "yes":
            self.dismiss(True)
        else:
            self.dismiss(False)

class PreviewPanel(Vertical):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        yield Label(id="name", classes="name")
        yield Label(id="updated_at", classes="date")
        # TODO: Add tags
        yield TextArea(id="text", classes="text", read_only=True)
        
    def display_note(self, note: Note):
        self.query_one("#name", expect_type=Label).update(note.name)
        self.query_one("#updated_at", expect_type=Label).update(note.updated_at.strftime("%Y-%m-%d %H:%M:%S"))
        self.query_one("#text", expect_type=TextArea).text = note.content

class NotesApp(App):
    CSS_PATH = ["ui_styles/notes_app.tcss", "ui_styles/preview_panel.tcss"]
    
    BINDINGS = [
        Binding("escape,f10", "quit", "Quit", show=True),
        Binding("a", "add", "Add note", show=True),
        Binding("v", "edit(False)", "View note", show=True),
        Binding("e", "edit(True)", "Edit note", show=True),
        Binding("d", "delete", "Delete note", show=True),
        Binding("s", "search", "Search note", show=True),
        Binding("p", "toggle_preview", "Toggle preview", show=True),
        
        
        # Binding("t", "add_tag", "Add tag", show=True),
        # Binding("r", "remove_tag", "Remove tag", show=True),
        # Binding("g", "view_tags", "View tags", show=True),
        # Binding("h", "help", "Help", show=True),
        # Binding("b", "back", "Back", show=True),
    ]

    def __init__(self, notebook: Notebook):
        super().__init__()
        self.notebook = notebook
        
    def compose(self) -> ComposeResult:
        with Container(id="container"):
            yield Input(placeholder="Search note", id="search_input")
            yield PreviewPanel(id="preview")
            yield DataTable(id="table").focus()
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = "row"
        
        preview = self.query_one("#preview", expect_type=PreviewPanel)
        preview.can_focus = False
        preview.can_focus_children = False
        
        self.list(self.notebook.notes)

    def on_input_changed(self, event: Input.Changed):
        if event.input.id == "search_input":
            self.list(self.notebook.search_notes(event.input.value))

    def action_quit(self):
        self.exit(0)

    def on_data_table_row_highlighted(self, e: DataTable.RowHighlighted):
        self.selected_row = e.row_key
        preview = self.query_one("#preview", expect_type=PreviewPanel)
        preview.display_note(self.notebook.get_note(self.selected_row))
        
    def action_search(self):
        search_input = self.query_one("#search_input", expect_type=Input)
        search_input.focus()
        
    async def action_edit(self, editable: bool):
        if not self.selected_row:
            return
        
        name = self.selected_row
        note = self.notebook.get_note(name)

        if not note:
            return
            
        def on_close(content: str):
            if content:
                self.notebook.edit_note(name, content)
                self.list(self.notebook.notes)
        
        screen = EditorScreen(note.name, note.content, editable, on_close=self.handle_editor_quit)
        self.push_screen(screen, on_close)
    
    async def action_delete(self):
        if not self.selected_row:
            return
        
        def on_close(result: bool):
            if result:
                self.notebook.delete_note(self.selected_row)
                console.print(f"Note '{self.selected_row}' deleted successfully.", style="green")
        
        screen = AskScreen(f"Are you sure you want to delete note '{self.selected_row}'?")
        self.push_screen(screen, on_close)
        
    def handle_editor_quit(self, question: str, on_close: Callable[[bool], None]):
        self.push_screen(AskScreen(question), on_close)

    def list(self, notes):
        table = self.query_one(DataTable)
        table.clear()
        table.columns.clear()
        table.add_columns("Name", "Updated At", "Content")

        for n in notes:
            table.add_row(n.name, n.updated_at, n.content[:20], key=n.name)
            
    def action_toggle_preview(self):
        preview = self.query_one("#preview", expect_type=PreviewPanel)
        preview.visible = not preview.visible
        
        container = self.query_one("#container", expect_type=Container)
        if preview.visible:
            container.remove_class("preview-hidden")
        else:
            container.add_class("preview-hidden")

@auto_save_on_error
def notes_main(notebook: Notebook):
    """
    Main loop for managing notes in the application.

    This function presents a GUI interface to the user for interacting with the notes section 
    of the application. It provides options for displaying a test message and exiting the program.
    """
    
    console.set_window_title("vNotes")
    
    app = NotesApp(notebook)
    app.run()
    
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


def add_note(notebook: Notebook, name):
    if(not name):
        name = input("Enter note name: ").strip()
    
    if(notebook.get_note(name)):
        console.print(f"Note '{name}' already exists.", style="yellow")
        return

    editor = NoteEditorApp(name)
    editor.run()

    notebook.add_note(name, editor.saved_content)
    console.print(f"Note '{name}' added successfully!", style="green")
