from addressbook_classes.field import Field
import re


class Phone(Field):

    def __init__(self, value):
        valid = bool(re.match(r"^\+380\d{9}$", value))
        if not valid:
            raise ValueError("Invalid phone number")
        self.value = value
