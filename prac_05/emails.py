"""
Word Occurrences
Estimate: 20 minutes
Actual:    minutes
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
