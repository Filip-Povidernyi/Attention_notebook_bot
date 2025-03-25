from name import Name
from phone import Phone
from email import Email
from address import Address
from birthday import Birthday


class Contact:
    def __init__(self, name):
        self.name = Name(name)
        self.email = None
        self.phone = []
        self.address = None
        self.birthday = None

    def __str__(self):

        birthday_str = f", birthday: {self.birthday.value.strftime('%d.%m.%Y')}" if self.birthday else ""
        address_str = f", address: {self.address.value}" if self.address else ""
        email_str = f", email: {self.email.value}" if self.email else ""
        return f"Contact name: {self.name.value.title()}, phones: {'; '.join(p.value for p in self.phones)}{birthday_str}{address_str}{email_str}"

    def add_email(self, email):
        self.email = Email(email)

    def add_phone(self, phone):
        self.phone.append(Phone(phone))

    def add_address(self, address):
        self.address = Address(address)

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
