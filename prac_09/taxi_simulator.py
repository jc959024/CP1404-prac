from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Main program to run the taxi simulator."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0

    print("Let's drive!")
    while True:
        choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
        if choice == 'q':
            break
        elif choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            total_bill += drive_taxi(current_taxi)
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display all available taxis with their index."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Prompt the user to choose a taxi by index."""
    display_taxis(taxis)
    taxi_choice = input("Choose taxi: ")
    if taxi_choice.isdigit():
        taxi_choice = int(taxi_choice)
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
    print("Invalid taxi choice")
    return None


def drive_taxi(taxi):
    """Drive the chosen taxi and return the fare."""
    if taxi:
        distance = float(input("Drive how far? "))
        taxi.start_fare()
        taxi.drive(distance)
        fare = taxi.get_fare()
        print(f"Your {taxi.name} trip cost you ${fare:.2f}")
        return fare
    else:
        print("You need to choose a taxi before you can drive")
        return 0


if __name__ == "__main__":
    main()
