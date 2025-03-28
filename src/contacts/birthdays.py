from datetime import date, timedelta

from .classes.contacts_book import ContactsBook
from .classes.contact import Contact


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
        print("You have no contacts in your contacts.")
        return

    print("\nShow birthdays within a given range from today.")

    while True:
        today = date.today()
        year_start = date(today.year, 1, 1)
        year_end = date(today.year, 12, 31)

        user_input = input("\nEnter number of days (positive for upcoming, negative for passed, 0 for today, empty for all): ").strip()

        if user_input == "":
            # Show all birthdays
            filtered_contacts = filter_contacts_by_date_range(contacts, year_start, year_end)
            print_birthday_contacts(filtered_contacts, year_start, year_end)
        else:
            if user_input == "today":
                days_range = 0
            else:
                try:
                    days_range = int(user_input)
                except ValueError:
                    print("Invalid input. Please enter a number or leave it blank.")
                    continue

            # Clamp start_date and end_date within -1 year to +1 year range
            # Compute min and max allowed dates, excluding the exact same day 
            # in the previous or next year
            # May be viable to use 'relativedelta' external library instead
            # min_allowed_date = today - relativedelta(years=1) + relativedelta(days=1)
            # max_allowed_date = today + relativedelta(years=1) - relativedelta(days=1)
            min_allowed_date = today - timedelta(days=364)  # 1 year back
            max_allowed_date = today + timedelta(days=364)  # 1 year ahead

            if days_range >= 0:
                # Today and Upcoming birthdays case
                start_date = today
                end_date = min(today + timedelta(days_range), max_allowed_date)   # Limit max +1 year

                if end_date > year_end:
                    # All birthdays that are in range from today until the end of the year
                    filtered_contacts = filter_contacts_by_date_range(contacts, start_date, year_end)
                    # Separate logic for the range beyond (after) the year_end
                    filtered_contacts += filter_contacts_by_date_range(contacts, year_end + timedelta(days=1), end_date)
                else:
                    # All birthdays within current year
                    filtered_contacts = filter_contacts_by_date_range(contacts, start_date, end_date)
                print_birthday_contacts(filtered_contacts, start_date, end_date)
            else:
                # Passed birthdays case
                start_date = max(today + timedelta(days_range), min_allowed_date)  # Limit max -1 year
                end_date = today

                if start_date < year_start:
                    # Separate logic for the range beyond (before) the year_start
                    filtered_contacts = filter_contacts_by_date_range(contacts, start_date, year_start - timedelta(days=1))
                    # All birthdays that are in range from the start of the year until today
                    filtered_contacts += filter_contacts_by_date_range(contacts, year_start, end_date)
                else:
                    # All birthdays within current year
                    filtered_contacts = filter_contacts_by_date_range(contacts, start_date, end_date)
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

    filtered_contacts.sort(key=lambda contact: contact.birthday.value.replace(year=today.year))

    return filtered_contacts

def print_birthday_contacts(contacts: list[Contact], start_date: date, end_date: date) -> None:
    """Prints the list of upcoming birthdays, formatted by date."""

    if not contacts:
        print("No birthdays found in this range.")
        return

    if start_date == end_date:
        date_range_str = f"{start_date.strftime('%d.%m')}"
        print(f"\nBirthdays for Today {date_range_str}:")
    else:
        date_range_str = f"{start_date.strftime('%d.%m')}" \
            f"{" (today)" if start_date == date.today() else ""}" \
            f" - {end_date.strftime('%d.%m')}" \
            f"{" (today)" if end_date == date.today() else ""}"
        print(f"\nBirthdays for {date_range_str}:")

    for contact in contacts:
        birthday = contact.birthday.value
        birthday_str = f"{birthday.day:02d}.{birthday.month:02d} ({birthday.strftime('%A')})"

        is_today = birthday.replace(year=date.today().year) == date.today()
        print(f"\n📅 {birthday_str}{" - today" if is_today else ""}:")

        email_str = f" ({contact.email.value})" if contact.email else ""
        print(f"    - {contact.name.value.title()}{email_str}")
