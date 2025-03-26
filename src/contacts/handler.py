from .classes.contact import Contact


def input_error(func):

    def inner(*args, **kwargs):

        try:
            return func(*args, **kwargs)

        except ValueError as e:
            return str(e)
        except KeyError as e:
            return str(e)
    return inner


exit_cmd = ('exit', 'close')


@input_error
def add_contact(book):

    while True:
        try:
            name = input("Enter a name: ").strip().lower()
            if name in exit_cmd:
                return None
            elif name:
                contact = Contact(name)
                break
        except ValueError as e:
            print(e)

    address = input("Enter address: ").strip().lower()
    if address in exit_cmd:
        return None
    elif address:
        contact.add_address(address)

    while True:
        try:
            phone = input("Enter phone: ").strip().lower()
            if phone in exit_cmd:
                return None
            elif phone:
                contact.add_phone(phone)
                break
            else:
                break
        except ValueError as e:
            print(e)

    while True:
        try:
            email = input("Enter email: ").strip().lower()
            if email in exit_cmd:
                return None
            elif email:
                contact.add_email(email)
                break
            else:
                break
        except ValueError as e:
            print(e)

    while True:
        try:
            birthday = input(
                "Enter birthday(Use DD.MM.YYYY): ").strip().lower()
            if birthday in exit_cmd:
                return None
            elif birthday:
                contact.add_birthday(birthday)
                break
            else:
                break
        except ValueError as e:
            print(e)

    book.add_contact(contact)

    return f"Contact added successfully!"


@input_error
def delete_contact(book):

    name = input("Enter a name: ").strip().lower()
    if name in exit_cmd:
        return None

    if book.find(name):
        book.delete(name)
        return f"Contact {name} deleted successfully!"


def show_all(book):

    if not book.data:
        return "No contacts in your phonebook"
    else:
        for record in book.data.values():
            print(f"{record}")
