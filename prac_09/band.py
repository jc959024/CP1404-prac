class Band:
    """Band class representing a band with a name and a list of musicians."""

    def __init__(self, name):
        """Construct a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of the band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def play(self):
        """Return a string showing each musician playing their first instrument."""
        return '\n'.join(musician.play() for musician in self.musicians)
