from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, TextArea
from textual.binding import Binding

class NoteEditor(App):
    CSS = """
    Screen {
        align: center middle;
    }

    TextArea {
        height: 80%;
        width: 90%;
        border: solid green;
    }
    """

    BINDINGS = [
        Binding("ctrl+s", "save", "Save", show=True),
        Binding("ctrl+q", "quit", "Quit", show=True),
    ]

    def __init__(self, initial_content: str = ""):
        super().__init__()
        self.content = initial_content
        self.saved_content = None

    def compose(self) -> ComposeResult:
        yield Header()
        yield TextArea(self.content)
        yield Footer()

    def on_mount(self) -> None:
        self.text_area = self.query_one(TextArea)
        self.text_area.focus()

    def action_save(self) -> None:
        self.saved_content = self.text_area.text
        self.notify("Content saved!")

    def action_quit(self) -> None:
        if not self.saved_content:
            self.saved_content = self.text_area.text
        self.exit()
