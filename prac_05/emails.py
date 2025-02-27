"""
Estimate: 20 minutes
Actual:   27 minutes
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        is_correct = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if is_correct not in ["", "y", "yes"]:
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


if __name__ == "__main__":
    main()
