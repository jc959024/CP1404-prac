def main():
    """Prompt the user for 5 numbers and store them in a list."""
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)

    print("Numbers entered:", numbers)  # Debugging step


main()
