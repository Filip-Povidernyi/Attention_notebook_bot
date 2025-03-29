from datetime import datetime
from rich.text import Text


class Note:
    def __init__(self, name):
        self.name = name
        self.create_at = datetime.now()
        self.updated_at = self.create_at
        self.content = ""
        self.tags = []

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
