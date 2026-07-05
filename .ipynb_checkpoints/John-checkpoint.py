name = []

while True:
    user_input = input("Enter a name:").lower()

    if user_input != "john":
        name.append(user_input)
        continue

    if user_input == "john":
        break

print(f"Incorrect names: {name}")
