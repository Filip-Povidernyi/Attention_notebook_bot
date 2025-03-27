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


exit_cmd = ['exit', 'close', 'back']


@input_error
def add_contact(book):

    while True:
        try:
            name = input("Enter a name: ").strip().lower()

            if name in exit_cmd:
                return "You back to menu."
            elif name:
                contact = Contact(name)
                break
        except ValueError as e:
            print(e)

    address = input("Enter address: ").strip().lower()

    if address in exit_cmd:
        return "You back to menu."
    elif address:
        contact.add_address(address)

    while True:
        try:
            phone = input("Enter phone: ").strip().lower()
            if phone in exit_cmd:
                return "You back to menu."
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
                return "You back to menu."
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
                return "You back to menu."
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
        return "You back to menu."

    if book.find(name):
        confirm = input(f"Are you sure you want to delete {name}? (yes/no): ")
        if confirm.lower() == "yes":
            book.delete(name)
            return f"Contact {name} deleted successfully!"
        else:
            return "Operation canceled."


@input_error
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
        return "You back to menu."

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
                cmd_phone = input(
                    "Do you want to add or change a phone? (add/change): ").strip().lower()

                if cmd_phone == "add":
                    new_phone = input("Enter a new phone: ").strip().lower()
                    contact.add_phone(new_phone)
                    return f"Contact phone added successfully!"
                else:
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


@input_error
def search_contacts(book):

    # Шукає контакти за ім'ям, телефоном, email, адресою або днем народження

    query = input("Enter search query: ").strip().lower()

    if query in exit_cmd:
        return None

    results = []

    for contact in book.data.values():
        if query.lower() in contact.name.value.lower():
            results.append(contact)

        elif contact.email and query.lower() in contact.email.value.lower():
            results.append(contact)

        elif any(query in phone.value for phone in contact.phones):
            results.append(contact)

        elif contact.address and query.lower() in contact.address.value.lower():
            results.append(contact)

        elif contact.birthday and query in contact.birthday.value.strftime('%d.%m.%Y'):
            results.append(contact)

    return results


handlers = {
    "add": add_contact,
    "delete": delete_contact,
    "show-all": show_all,
    "edit": edit_contact,
    "find": search_contacts
}
