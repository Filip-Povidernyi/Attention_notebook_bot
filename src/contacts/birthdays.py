def get_upcoming_birthdays():
    """
    Displays upcoming birthdays within a specified number of days from today.

    This function prompts the user to enter a number of days to filter upcoming 
    birthdays. If a valid number is provided, it displays birthdays within that 
    range.

    The user can leave the input blank to show all birthdays.
    """
    print("Show all upcoming birthdays in days range from now.")

    while True:
        user_input = input("Please, enter number of days (or leave it blank to show all birthdays): ")
        
        if user_input.isdigit():
            days_range = int(user_input)
            print(f"Print birthdays in \"{days_range}\" days range")
        else:
          print("Invalid non-number days value. Please try again.")
