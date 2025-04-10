from taxi import Taxi


# Create a new taxi object
my_taxi = Taxi("Prius 1", 100)

# Drive 40 km
my_taxi.drive(40)

# Print details and fare
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")

# Start a new fare and drive 100 km
my_taxi.start_fare()
my_taxi.drive(100)

# Print details and fare
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")
