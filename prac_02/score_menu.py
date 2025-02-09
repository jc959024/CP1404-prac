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


def evaluate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_valid_score():
    while True:
        try:
            score = float(input("Enter score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def print_result(score):
    result = evaluate_score(score)
    print(result)


def show_stars(score):
    print('*' * int(score))


def display_menu():
    print(MENU)


main()
