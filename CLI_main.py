from CLI_Bot.AddressBook.addressbook_main import addressbook_main


def main():
    print("Hello! How i can help you?")
    print('For enter to addressbook enter "1"')
    print('For enter to notes enter "2"')
    print('For exit enter "exit" or "close"')

    while True:

        cmd = input("Enter a command: ").strip().lower()

        if cmd == '1':
            addressbook_main()

        elif cmd == '2':
            pass

        elif cmd == 'exit' or cmd == 'close':
            print("Goodbye!")
            break

        else:
            print("Unknown command. Please try again.")


if __name__ == '__main__':
    main()
