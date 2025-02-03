LOW_SALES_THRESHOLD = 1000
LOW_SALES_BONUS_RATE = 0.1
HIGH_SALES_BONUS_RATE = 0.15

sales = float(input("Enter sales: $"))

if sales >= 0:
    if sales < LOW_SALES_THRESHOLD:
        bonus = sales * LOW_SALES_BONUS_RATE
    else:
        bonus = sales * HIGH_SALES_BONUS_RATE
    print("Bonus: $", bonus)
else:
    print("Invalid sales amount.")


