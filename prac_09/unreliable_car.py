import random
from car import Car


class UnreliableCar(Car):
    """A Car that has a reliability factor affecting its ability to drive."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance with name, fuel, and reliability."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Attempt to drive the given distance.
        Only drives if a random number is less than the car's reliability.
        Returns the distance driven (maybe 0).
        """
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0
