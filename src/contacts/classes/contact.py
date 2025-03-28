from .address import Address
from .birthday import Birthday
from .email import Email
from .name import Name
from .phone import Phone


class Contact:
    def __init__(self, name):
        self.name = Name(name)
        self.email = None
        self.phones = []
        self.address = None
        self.birthday = None

    def __str__(self):

        birthday_str = f", birthday: {self.birthday.value.strftime('%d.%m.%Y')}" if self.birthday else ""
        address_str = f", address: {self.address.value}" if self.address else ""
        email_str = f", email: {self.email.value}" if self.email else ""
        return f"Contact name: {self.name.value.title()}, phones: {'; '.join(p.value for p in self.phones)}{birthday_str}{address_str}{email_str}"

    def add_email(self, email: str):
        self.email = Email(email)

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def add_address(self, address: str):
        self.address = Address(address)

    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)

    def edit_phone(self, old_phone: str, new_phone: str):

        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = Phone(new_phone).value

                return f"Номер {old_phone} змінено на номер {new_phone}"

        raise ValueError(f"Номер {old_phone} не знайдено")
