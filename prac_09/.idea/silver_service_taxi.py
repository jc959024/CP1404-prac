from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A fancy taxi with flagfall and higher price per km."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise name, fuel, fanciness, and adjust price per km."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return fare including flagfall."""
        return self.flagfall + super().get_fare()

    def __str__(self):
        """Return string with fare details and flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
