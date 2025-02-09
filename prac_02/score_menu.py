MENU = """
Menu:
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
"""


def main():
    score = get_valid_score()

    while True:
        display_menu()
        choice = input("Choose an option: ").strip().upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell!")
            break
        else:
            print("Invalid choice.")
