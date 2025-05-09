from .classes.contact import Contact
from .classes.contacts_book import ContactsBook
from src.utils.autocomplete import suggest_command
from rich.console import Console
from rich.table import Table
from ..utils.common import print_help
from ..utils.constants import CONTACT_MENU_COMMANDS

console = Console()


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
commands = ["name", "phone", "address", "email", "birthday"]


@input_error
def add_contact(book):
    console.print(
        "For back to menu, enter [red]back[/red].\n", style="steel_blue")
    while True:
        try:
            name = input("Enter a name: ").strip().lower()

            if name in exit_cmd:
                console.print("You back to menu.", style="green")
                print_help(CONTACT_MENU_COMMANDS)
                return
            elif name:
                contact = Contact(name)
                break
        except ValueError as e:
            console.print(f"{e}", style="red")

    address = input("Enter address: ").strip().lower()

    if address in exit_cmd:
        console.print("You back to menu.", style="green")
        print_help(CONTACT_MENU_COMMANDS)
        return
    elif address:
        contact.add_address(address)

    while True:
        try:
            phone = input("Enter phone: ").strip().lower()
            if phone in exit_cmd:
                console.print("You back to menu.", style="green")
                print_help(CONTACT_MENU_COMMANDS)
                return
            elif phone:
                contact.add_phone(phone)
                break
            else:
                break
        except ValueError as e:
            console.print(f"{e}", style="red")

    while True:
        try:
            email = input("Enter email: ").strip().lower()
            if email in exit_cmd:
                console.print("You back to menu.", style="green")
                print_help(CONTACT_MENU_COMMANDS)
                return
            elif email:
                contact.add_email(email)
                break
            else:
                break
        except ValueError as e:
            console.print(f"{e}", style="red")

    while True:
        try:
            birthday = input(
                "Enter birthday(Use DD.MM.YYYY): ").strip().lower()
            if birthday in exit_cmd:
                console.print("You back to menu.", style="green")
                print_help(CONTACT_MENU_COMMANDS)
                return
            elif birthday:
                contact.add_birthday(birthday)
                break
            else:
                break
        except ValueError as e:
            console.print(f"{e}", style="red")

    book.add_contact(contact)

    return f"Contact added successfully!"


@input_error
def delete_contact(book):

    console.print(
        "For back to menu, enter [red]back[/red].\n", style="steel_blue")
    name = input("Enter a name to delete: ").strip().lower()

    if name in exit_cmd:
        console.print("You back to menu.", style="green")
        print_help(CONTACT_MENU_COMMANDS)
        return

    if book.find(name):

        console.print(
            f"Are you sure you want to delete {name.title()}? (yes/no):", style="red")
        confirm = input().strip().lower()

        if confirm == "yes" or confirm == "y":
            book.delete(name)
            return f"Contact {name} deleted successfully!"
        elif confirm == "no" or confirm == "n":
            return "Operation canceled."


@input_error
def show_all(book):

    if isinstance(book, ContactsBook):
        if not book.data:
            console.print(
                "[bold yellow]You got no contacts yet![/bold yellow]")
            return

        table = Table(title="Contacts")

        table.add_column("Name", style="cyan", no_wrap=True)
        table.add_column("Phones", style="magenta")
        table.add_column("Email", style="blue")
        table.add_column("Addres", style="green")
        table.add_column("Birthday", style="yellow")

        for contact in book.data.values():
            table.add_row(
                contact.name.value.title(),
                ", ".join(p.value for p in contact.phones) or "-",
                contact.email.value if contact.email else "-",
                contact.address.value.title() if contact.address else "-",
                contact.birthday.value.strftime(
                    "%d.%m.%Y") if contact.birthday else "-"
            )

        return table

    elif isinstance(book, list):
        if not book:
            console.print(
                "[bold yellow]No matches found![/bold yellow]")
            return

        table = Table(title="Search results")

        table.add_column("Name", style="cyan", no_wrap=True)
        table.add_column("Phones", style="magenta")
        table.add_column("Email", style="blue")
        table.add_column("Addres", style="green")
        table.add_column("Birthday", style="yellow")

        for contact in book:
            table.add_row(
                contact.name.value.title(),
                ", ".join(p.value for p in contact.phones) or "-",
                contact.email.value if contact.email else "-",
                contact.address.value.title() if contact.address else "-",
                contact.birthday.value.strftime(
                    "%d.%m.%Y") if contact.birthday else "-"
            )

        return table


# @input_error
def edit_contact(book):

    console.print(
        "For back to menu, enter [red]back[/red].\n", style="steel_blue")
    name = input("Enter a name: ").strip().lower()

    if name in exit_cmd:
        console.print("You back to menu.", style="green")
        print_help(CONTACT_MENU_COMMANDS)
        return

    if book.find(name):
        contact = book.data[name]
        console.print(show_all([contact]))

        while True:
            cmd = input(
                "\nWhat do you want to change? (name/phone/address/email/birthday): ").strip().lower()

            if cmd in exit_cmd:
                console.print("You back to menu.", style="green")
                print_help(CONTACT_MENU_COMMANDS)
                return

            elif cmd == "name":

                new_name = input("Enter a new name: ").strip().lower()

                if new_name != name and not book.find(new_name):
                    book.data[new_name] = contact
                    book.data[new_name].name.value = new_name
                    book.delete(name)
                console.print(
                    "Contact name changed successfully!", style="green")

            elif cmd == "phone":
                while True:
                    cmd_phone = input(
                        "\nDo you want to add, change or remove a phone? (add/change/remove): ").strip().lower()

                    if cmd_phone in exit_cmd:
                        break
                    if cmd_phone == "add":
                        while True:
                            new_phone = input(
                                "Enter a new phone: ").strip().lower()
                            if new_phone in exit_cmd:
                                break
                            else:
                                try:
                                    contact.add_phone(new_phone)
                                    console.print(
                                        "Contact phone added successfully!", style="green")
                                    break
                                except ValueError as e:
                                    console.print(e, style="red")

                    elif cmd_phone == "change":
                        while True:
                            old_phone = input(
                                "Enter a old phone: ").strip().lower()
                            if old_phone in [p.value for p in contact.phones] and old_phone not in exit_cmd:
                                new_phone = input(
                                    "Enter a new phone: ").strip().lower()
                                if new_phone in exit_cmd:
                                    break
                                else:
                                    try:
                                        contact.edit_phone(
                                            old_phone, new_phone)
                                        console.print(
                                            "Contact phone changed successfully!", style="green")
                                        break
                                    except ValueError as e:
                                        console.print(e, style="red")
                            elif old_phone in exit_cmd:
                                break
                            else:
                                console.print(
                                    f"This phone namber is absent in contact {name.title()}. Try again!", style="yellow")

                    elif cmd_phone == "remove":
                        rem_phone = input(
                            "Enter a phone number for remove: ").strip().lower()
                        if rem_phone in exit_cmd:
                            break
                        else:
                            if rem_phone in [p.value for p in contact.phones]:
                                contact.remove_phone(rem_phone)
                                console.print(
                                    "Contact phone removed successfully!", style="green")
                                break
                            else:
                                console.print(
                                    f"This phone namber is absent in contact {name.title()}. Try again!", style="yellow")
                    else:
                        suggested = suggest_command(
                            cmd_phone, ['add', 'change', 'remove'] + exit_cmd, 0.5)
                        if suggested:
                            console.print(
                                f"Unknown command '{cmd_phone}'.\nMaybe you mean '{suggested}'?", style="deep_pink4")
                        else:
                            console.print(
                                f"Unknown command '{cmd_phone}'. Please try again.", style="deep_pink4")

            elif cmd == "address":
                while True:
                    new_address = input(
                        "Enter a new address: ").strip().lower()
                    if new_address in exit_cmd:
                        break
                    contact.add_address(new_address)
                    console.print(
                        "Contact address changed successfully!", style="green")
                    break

            elif cmd == "email":
                while True:
                    new_email = input("Enter a new email: ").strip().lower()
                    if new_email in exit_cmd:
                        break
                    else:
                        try:
                            contact.add_email(new_email)
                            console.print(
                                "Contact email changed successfully!", style="green")
                            break
                        except ValueError as e:
                            console.print(e, style="red")

            elif cmd == "birthday":
                while True:
                    new_birthday = input(
                        "Enter a new birthday(Use DD.MM.YYYY): ").strip().lower()
                    if new_birthday in exit_cmd:
                        break
                    else:
                        try:
                            contact.add_birthday(new_birthday)
                            console.print(
                                "Contact birthday changed successfully!", style="green")
                            break
                        except ValueError as e:
                            console.print(e, style="red")

            else:
                suggested = suggest_command(cmd, commands + exit_cmd, 0.5)
                if suggested:
                    console.print(
                        f"Unknown command '{cmd}'.\nMaybe you mean '{suggested}'?", style="deep_pink4")

                else:
                    console.print(
                        f"Unknown command '{cmd}'. Please try again.", style="deep_pink4")
    else:
        return f"Contact {name} not found in your phonebook"


@input_error
def search_contacts(book):

    # Шукає контакти за ім'ям, телефоном, email, адресою або днем народження
    console.print(
        "For back to menu, enter [red]back[/red].\n", style="steel_blue")

    results = []

    while True:
        query = input("Enter search query: ").strip().lower()

        if query in exit_cmd:
            return None

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

        if not results:
            console.print(
                "\nNo contacts found matching your query. Try again!\n", style="red")
            continue
        else:
            return results


handlers = {
    "add": add_contact,
    "delete": delete_contact,
    "show-all": show_all,
    "edit": edit_contact,
    "find": search_contacts
}
