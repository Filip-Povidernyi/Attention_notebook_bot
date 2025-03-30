from rich.console import Console
from rich.table import Table
from rich.box import ROUNDED


def print_help(commands: dict[str, str]):
    """Prints a formatted list of available commands and their descriptions in a table."""
    # Створення консолі
    console = Console()

    # Створення таблиці
    table = Table(title="", box=ROUNDED, show_header=True)

    # Додавання стовпців
    table.add_column("Command", style="bold cyan")
    table.add_column("Description", style="green")

    # Додавання рядків до таблиці
    for cmd, desc in commands.items():
        table.add_row(cmd, desc)

    # Виведення таблиці
    console.print(table)
