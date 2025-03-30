from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich.box import ROUNDED

def print_note_table(note):
    table = Table(title="", box=ROUNDED, show_header=True)

    # Создаем заголовок
    title_text = Text(f"Note {note.name}")

    if note.tags:
        tag_text = Text()
        tag_text.append("\nTags: ", style="bold")
        tag_text.append(", ".join(note.tags))
        title_text.append(tag_text)

    table.add_column(str(title_text))  # Преобразуем в строку, чтобы избежать ошибок

    # Контент
    text = Text(note.content or "", style="white")  # Проверка, что note.content не None
    console = Console()
    table.add_row(text)

    # Дата обновления
    if note.updated_at:
        table.add_row(Text(f"\n\nLast updated: {note.updated_at.strftime('%Y-%m-%d %H:%M:%S')}", style="dim italic"))

    # Вывод в консоль
    console.print(table)