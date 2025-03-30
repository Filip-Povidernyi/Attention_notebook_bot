from .field import Field


class Name(Field):

    def __init__(self, value):

        if len(value) < 2:
            raise ValueError(
                "Name is too short. Should be at least 2 characters. Try again.")
        else:
            super().__init__(value)
            self.value = value
