def command_parser(command):

    cmd, *args = command.split(' ')
    cmd = cmd.strip().lower()

    return cmd, args


def main():

    print("Hello! How i can help you?")

    while True:

        command_line = input("Enter a command: ").strip().lower()
        cmd, args = command_parser(command_line)

        if cmd == 'add':
            pass

        elif cmd == 'exit' or cmd == 'close':
            pass

        else:
            print("Unknown command. Please try again.")
