from textual.app import Widget, ComposeResult
from textual.widgets import TextArea

class NoteEditor(Widget):

    def __init__(self, initial_content: str = "", editable: bool = False, **kwargs):
        super().__init__(**kwargs)
        self.initial_content = initial_content
        self.saved_content = None
        self.editable = editable

    def compose(self) -> ComposeResult:
        yield TextArea(self.initial_content, classes="editor", show_line_numbers=True, read_only=(not self.editable))

    def on_mount(self) -> None:
        self.text_area = self.query_one(TextArea)
        self.text_area.focus()
        
    def get_text(self) -> str:
        return self.text_area.text

