"""
Word Occurrences
Estimate: 30 minutes
Actual:   32 minutes
"""
from guitar import Guitar


def main():
    guitars = [
        Guitar("Gibson L-5 CES", 1922, 16035.40),
        Guitar("Line 6 JTV-59", 2010, 1512.90)
    ]

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")

    if guitars:
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars :( Maybe buy one?")


if __name__ == "__main__":
    main()
