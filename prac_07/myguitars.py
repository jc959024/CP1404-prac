import csv
from guitar import Guitar


def read_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                name, year, cost = row
                guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def print_guitars(guitars):
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


def add_new_guitars(guitars):
    print("Enter your new guitars (leave name blank to stop):")
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
    return guitars


def write_guitars(filename, guitars):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def main():
    filename = "guitars.csv"
    guitars = read_guitars(filename)
    guitars = add_new_guitars(guitars)
    guitars.sort()
    write_guitars(filename, guitars)
    print("\nThese are your guitars:")
    print_guitars(guitars)


if __name__ == '__main__':
    main()
