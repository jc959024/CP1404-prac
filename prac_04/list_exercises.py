def main():
    """Main function to run number statistics and user authentication."""
    number_statistics()
    user_authentication()


def number_statistics():
    """Prompt the user for 5 numbers, store them in a list, and display statistics."""
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")


def user_authentication():
    """Check if the entered username is in the list of authorized users."""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    username = input("Enter your username: ")

    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()

