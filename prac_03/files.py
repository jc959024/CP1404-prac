name = input("Please enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)
