name = input("Please enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)

with open("name.txt", "r") as file:
    name = file.read().strip()
print(f"Hi {name}!")

with open("numbers.txt", "r") as file:
    first_number = int(file.readline().strip())
    second_number = int(file.readline().strip())

result = first_number + second_number
print(result)
