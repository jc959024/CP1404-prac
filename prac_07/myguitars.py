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


def main():
    filename = "guitars.csv"
    guitars = read_guitars(filename)
    print("\nThese are your guitars:")
    print_guitars(guitars)


if __name__ == '__main__':
    main()
