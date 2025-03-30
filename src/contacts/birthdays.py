from collections import defaultdict

from datetime import date
from dateutil.relativedelta import relativedelta

from .classes.contacts_book import ContactsBook
from .classes.contact import Contact
from rich.console import Console
from rich.table import Table

console = Console()

def get_upcoming_birthdays(book: ContactsBook) -> None:
    """
    Displays birthdays within a specified number of days from today.

    This function prompts the user to enter a number of days to filter and show
    birthdays. 

    If a valid number is provided, it displays birthdays within that range.

    The user can leave the input blank to show all birthdays.
    """

    contacts = list(book.data.values())

    if not contacts:
        console.print("You have no contacts in your contacts.",
                      style="steel_blue")
        return

    console.print(
        "\nShow birthdays within a given range from today.", style="steel_blue")

    while True:
        today = date.today()
        year_start = date(today.year, 1, 1)
        year_end = date(today.year, 12, 31)

        user_input = input(
            "\nEnter number of days (positive for upcoming, negative for passed, 0 for today, empty for all): ").strip()

        if user_input == "":
            # Show all birthdays
            filtered_contacts = filter_contacts_by_date_range(
                contacts, year_start, year_end)
            print_birthday_contacts(filtered_contacts, year_start, year_end)
            return

        if user_input == "today":
            days_range = 0
        else:
            try:
                days_range = int(user_input)
            except ValueError:
                console.print(
                    "Invalid input. Please enter a number or leave it blank.", style="yellow")
                continue

        if days_range >= 0:
            # Today and Upcoming birthdays case
            start_date = today
            max_allowed_date = today + \
                relativedelta(years=1) - \
                relativedelta(days=1)  # Clamp 1 year ahead
            end_date = min(today + relativedelta(days=days_range),
                           max_allowed_date)  # Limit max +1 year

            if end_date > year_end:
                # All birthdays that are in range from today until the end of the year
                filtered_contacts = filter_contacts_by_date_range(
                    contacts, start_date, year_end)
                # Separate logic for the range beyond (after) the year_end
                filtered_contacts += filter_contacts_by_date_range(
                    contacts, year_end + relativedelta(days=1), end_date)
            else:
                # All birthdays within current year
                filtered_contacts = filter_contacts_by_date_range(
                    contacts, start_date, end_date)
            print_birthday_contacts(filtered_contacts, start_date, end_date)
        else:
            # Passed birthdays case
            min_allowed_date = today - \
                relativedelta(years=1) + \
                relativedelta(days=1)  # Clamp 1 year back
            start_date = max(today + relativedelta(days=days_range),
                             min_allowed_date)  # Limit max -1 year
            end_date = today

            if start_date < year_start:
                # Separate logic for the range beyond (before) the year_start
                filtered_contacts = filter_contacts_by_date_range(
                    contacts, start_date, year_start - relativedelta(days=1))
                # All birthdays that are in range from the start of the year until today
                filtered_contacts += filter_contacts_by_date_range(
                    contacts, year_start, end_date)
            else:
                # All birthdays within current year
                filtered_contacts = filter_contacts_by_date_range(
                    contacts, start_date, end_date)
            print_birthday_contacts(filtered_contacts, start_date, end_date)
        return


def filter_contacts_by_date_range(contacts: list[Contact], start_date: date, end_date: date) -> list[Contact]:
    """Filters contacts whose birthdays fall within the given date range."""
    today = date.today()
    start_date = start_date.replace(year=today.year)
    end_date = end_date.replace(year=today.year)

    filtered_contacts = [
        contact for contact in contacts
        if contact.birthday
        and start_date <= contact.birthday.value.replace(year=today.year) <= end_date
    ]

    filtered_contacts.sort(
        key=lambda contact: contact.birthday.value.replace(year=today.year))

    return filtered_contacts


def print_birthday_contacts(contacts: list[Contact], start_date: date, end_date: date) -> None:
    """Prints the list of upcoming birthdays, formatted by date."""

    if not contacts:
        console.print("No birthdays found in this range.", style="red1")
        return

    # Format the date range header
    today_str = " (today)"
    start_part = f"{start_date.strftime('%d.%m')}{today_str if start_date == date.today() else ''}"
    end_part = f"{end_date.strftime('%d.%m')}{today_str if end_date == date.today() else ''}"

    date_range_str = f"{start_part} - {end_part}" if start_date != end_date else start_part
    console.print(f"\nBirthdays for {date_range_str}:", style="steel_blue")

    # Group contacts by birthday
    grouped_contacts = defaultdict(list)
    for contact in contacts:
        birthday_key = f"📅 {contact.birthday.value.strftime('%d.%m (%A)')}"
        grouped_contacts[birthday_key].append(contact)

    # Create and populate the table
    table = Table(show_header=True, header_style="bold")
    table.add_column("Birthday date", style="yellow")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Email", style="blue")
    table.add_column("Phones", style="magenta")

    max_name_length = max(
        (len(contact.name.value) for contacts in grouped_contacts.values() for contact in contacts),
        default=0  # Ensure it's safe in case there are no contacts
    )

    for birthday_str, contacts in grouped_contacts.items():

        for contact in contacts:

            birthday_date = contact.birthday.value.replace(year=date.today().year)
            is_today = birthday_date == date.today()

            if is_today:
                birthday_str = f"{birthday_str} ← today"
            
            phones_details = []
            if contact.phones:
                phones_details.extend(phone.value for phone in contact.phones)
            
            table.add_row(
                birthday_str, 
                f'{contact.name.value.title().ljust(max_name_length + 3) + "🎂"}',
                contact.email.value if contact.email else "-",
                ", ".join(phones_details) if phones_details else "-"
            )

    console.print(table)
