def get_upcoming_birthdays():
    print("Show all upcoming birthdays in days range from now.")

    while True:
        cmd = input("Please, enter number of days (or leave it blank to show all birthdays): ")
        
        try:
            days_range = int(cmd)
            print(f"Print birthdays in {days_range} days range")
            return days_range
        
        except ValueError:
          print("Invalid days value. Please try again.")
