from .field import Field
import re


class Email(Field):
    def __init__(self, value: str):

        valid = bool(
            re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", value))
        if not valid:
            raise ValueError("Invalid email address")
        self.value = value
