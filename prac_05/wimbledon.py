"""
Estimate: 20 minutes
Actual:   35 minutes
"""
import csv


def read_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        return in_file.readlines()[1:]  # Skip the header row


def process_data(lines):
    champions = {}
    countries = set()
    for line in lines:
        parts = line.strip().split(',')
        champion = parts[1]
        country = parts[2]
        champions[champion] = champions.get(champion, 0) + 1
        countries.add(country)
    return champions, countries


def sort_and_display_champions(champions):
    for champion, wins in sorted(champions.items(), key=lambda item: item[1], reverse=True):
        print(f"{champion} {wins}")


def sort_and_display_countries(countries):
    sorted_countries = sorted(countries)
    print("These countries have won Wimbledon:", ', '.join(sorted_countries))


def main():
    filename = "wimbledon.csv"
    lines = read_file(filename)
    champions, countries = process_data(lines)
    print("Wimbledon Champions:")
    sort_and_display_champions(champions)
    print()
    sort_and_display_countries(countries)


if __name__ == "__main__":
    main()
