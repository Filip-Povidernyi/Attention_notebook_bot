from textual.widgets import ListView as BaseListView, ListItem, Label
from textual.containers import Vertical

class ListView(BaseListView):
    def __init__(self, *items):
        super().__init__(*items)
    
    def add(self, item: ListItem):
        """Добавляет элемент в ListView."""
        self.mount(item)
    
    def clear(self):
        """Очищает ListView."""
        self.remove_children()

__all__ = ["ListView", "ListItem", "Label"]
