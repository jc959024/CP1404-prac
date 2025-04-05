from silver_service_taxi import SilverServiceTaxi


def main():
    """Test the SilverServiceTaxi class with a sample car and print results."""
    silver_car = SilverServiceTaxi("Hummer", 200, 2)
    print(silver_car)

    silver_car.drive(18)
    print(silver_car)

    print(f"Fare: ${silver_car.get_fare():.2f}")


main()
