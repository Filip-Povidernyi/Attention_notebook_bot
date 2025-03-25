from AddressBook.addressbook_classes.contact import Contact


def input_error(func):

    def inner(*args, **kwargs):

        try:
            return func(*args, **kwargs)

        except ValueError as e:
            return str(e)

    return inner


@input_error
def add_contact(book):

    exit_cmd = ('exit', 'close')

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
