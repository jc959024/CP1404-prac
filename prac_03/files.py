name = input("Please enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)

with open("name.txt", "r") as file:
    name = file.read().strip()
print(f"Hi {name}!")

with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

if len(numbers) >= 2:
    result = numbers[0] + numbers[1]
    print(result)

total = sum(numbers)
print(total)