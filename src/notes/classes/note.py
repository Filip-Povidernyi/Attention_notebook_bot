from datetime import datetime


class Note:
    def __init__(self, name):
        self.name = name
        self.create_at = datetime.now()
        self.updated_at = self.create_at
        self.content = ""
        self.tags = []

    def __str__(self):
        return f"Note name: {self.name}, {self.updated_at.strftime('%Y-%m-%d %H:%M:%S')} {self.content[:20]}..."
    
    def set_content(self, content):
        self.content = content
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

