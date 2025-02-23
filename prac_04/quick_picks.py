import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    number_of_picks = int(input("How many quick picks? "))
    for _ in range(number_of_picks):
        quick_pick = sorted(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_PICK))
        print(" ".join(f"{number:2}" for number in quick_pick))


if __name__ == "__main__":
    main()