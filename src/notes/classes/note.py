from datetime import datetime


class Note:
    def __init__(self, name):
        self.name = name
        self.createAt = datetime.now()
        self.updatedAt = self.createAt
        self.content = ""
        self.tags = []

    def __str__(self):
        return f"Note name: {self.name}, {self.updatedAt.strftime('%Y-%m-%d %H:%M:%S')} {self.content[:20]}..."
    
    def setContent(self, content):
        self.content = content
        self.updatedAt = datetime.now()

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

