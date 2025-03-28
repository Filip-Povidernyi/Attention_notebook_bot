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

    def __init__(self, title, initial_content: str = ""):
        super().__init__()
        self.title = title
        self.initial_content = initial_content
        self.saved_content = None

    def compose(self) -> ComposeResult:
        yield Header(name=self.title)
        yield TextArea(self.initial_content)
        yield Footer()

    def on_mount(self) -> None:
        self.text_area = self.query_one(TextArea)
        self.text_area.focus()

    def action_save(self) -> None:
        self.saved_content = self.text_area.text
        self.notify("Content saved!")

    def action_quit(self) -> None:
        self.exit()
