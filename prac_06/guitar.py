"""
Word Occurrences
Estimate: 20 minutes
Actual:   13 minutes
"""


class Guitar:
    CURRENT_YEAR = 2024
    VINTAGE_AGE = 50

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        return self.CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= self.VINTAGE_AGE
