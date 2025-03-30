from .field import Field
from datetime import datetime


class Birthday(Field):

    def __init__(self, value: str):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError(
                f'Invalid date format. Use DD.MM.YYYY\n'f"Or day {value} is out of range for month")

    def __str__(self):
        return f"📅{self.value.strftime('%d.%m.%Y')}"
