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


exit_cmd = ['exit', 'close']


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


@input_error
def edit_contact(book):

    name = input("Enter a name: ").strip().lower()
    if name in exit_cmd:
        return None

    if book.find(name):
        contact = book.data[name]
        print(f"Contact name: {contact.name.value.title()}")
        print(f"Phones: {', '.join(p.value for p in contact.phones)}")
        if contact.address:
            print(f"Address: {contact.address.value.title()}")
        else:
            print("Address: None")
        if contact.email:
            print(f"Email: {contact.email.value}")
        else:
            print("Email: None")
        if contact.birthday:
            print(f"Birthday: {contact.birthday.value.strftime('%d.%m.%Y')}")
        else:
            print("Birthday: None")

        while True:
            cmd = input(
                "What do you want to change? (name, phone, address, email, birthday): ").strip().lower()

            if cmd == "name":
                new_name = input("Enter a new name: ").strip().lower()
                contact.name.value = new_name
                return f"Contact name changed successfully!"

            elif cmd == "phone":
                old_phone = input("Enter a old phone: ").strip().lower()
                new_phone = input("Enter a new phone: ").strip().lower()
                contact.edit_phone(old_phone, new_phone)
                return f"Contact phone changed successfully!"

            elif cmd == "address":
                new_address = input("Enter a new address: ").strip().lower()
                contact.add_address(new_address)
                return f"Contact address changed successfully!"

            elif cmd == "email":
                new_email = input("Enter a new email: ").strip().lower()
                contact.add_email(new_email)
                return f"Contact email changed successfully!"

            elif cmd == "birthday":
                new_birthday = input(
                    "Enter a new birthday(Use DD.MM.YYYY): ").strip().lower()
                contact.add_birthday(new_birthday)
                return f"Contact birthday changed successfully!"

            else:
                return "Unknown command. Please try again."
    else:
        return f"Contact {name} not found in your phonebook"
