from .field import Field
import re


class Phone(Field):

    def __init__(self, value):
        valid = bool(re.match(r"^(\+380|0)\d{9}$", value))
        if not valid:
            raise ValueError(
                "Invalid phone number. Valid format is +380XXXXXXXXX or 0XXXXXXXXX")
        self.value = value
