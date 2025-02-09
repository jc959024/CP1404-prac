MIN_LENGTH = 7


def main():
    password = get_password()
    print_password_asterisks(password)


def get_password():
    password = input("Please enter your password:")

    while len(password) < MIN_LENGTH:
        print("Invalid password. At least 7 characters long.")
        password = input("Please enter your password:")

    return password


def print_password_asterisks(password):
    print("*" * len(password))
