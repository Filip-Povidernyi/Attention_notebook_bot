from datetime import datetime
from rich.console import Console
from rich.text import Text


class Note:
    def __init__(self, name):
        self.name = name
        self.create_at = datetime.now()
        self.updated_at = self.create_at
        self.content = ""
        self.tags = []

    def __str__(self):

        text = Text()
        text.append(f"Note name: {str(self.name)}", style="bold cyan")
        text.append(
            f"\nLast updated: {self.updated_at.strftime('%Y-%m-%d %H:%M:%S')}", style="italic")
        if self.tags:
            text.append("\nTags: ", style="bold")
            text.append(", ".join(self.tags), style="yellow")
        text.append("\nContent: \n", style="bold")
        text.append(str(self.content), style="white")
        return str(text)

    def set_content(self, content):
        self.content = content if content is not None else ""
        self.updated_at = datetime.now()

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)
            return True
        return False

    def remove_tag(self, tag: str):
        if tag in self.tags:
            self.tags.remove(tag)
            return True
        return False

    def view_tags(self):
        return self.tags
