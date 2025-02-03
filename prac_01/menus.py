MENU = """
(H)ello
(G)oodbye
(Q)uit
"""


def main():
    name = input("Enter name: ")
    display_menu = True
    while display_menu:
        print(MENU)
        choice = input(">>> ").upper()

        if choice == "Q":
            print("Finished.")
            display_menu = False
        elif choice == "H":
            print("Hello", name)
        elif choice == "G":
            print("Goodbye", name)
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
