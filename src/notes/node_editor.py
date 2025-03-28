from textual.app import App, Widget, ComposeResult
from textual.widgets import Header, Footer, TextArea
from textual.binding import Binding

class NoteEditorApp(App):
    CSS = """
    Screen {
        align: center middle;
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
        yield NoteEditor(name=self.title, initial_content=self.initial_content)

    def on_mount(self) -> None:
        pass
        # self.text_area = self.query_one(TextArea)
        # self.text_area.focus()

    def action_save(self) -> None:
        editor = self.query_one(NoteEditor)
        self.saved_content = editor.get_text()
        self.notify("Content saved!")

    def action_quit(self) -> None:
        self.exit()

class NoteEditor(Widget):
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
        
    def get_text(self) -> str:
        return self.text_area.text

