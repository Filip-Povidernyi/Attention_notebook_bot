from datetime import datetime


class Note:
    def __init__(self, name):
        self.name = name
        self.createAt = datetime.now()
        self.updatedAt = self.createAt
        self.content = ""

    def __str__(self):
        return f"Note name: {self.name}, TODO..."
    
    def setContent(self, content):
        self.content = content
        self.updatedAt = datetime.now()

