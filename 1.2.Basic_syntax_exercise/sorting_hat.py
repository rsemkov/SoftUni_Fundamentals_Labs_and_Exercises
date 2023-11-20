all_sorted = True
while True:
    name = input()
    if name == "Welcome!":
        break
    elif name == "Voldemort":
        all_sorted = False
        print("You must not speak of that name!")
        break

    name_length = len(name)

    if name_length < 5:
        print(f"{name} goes to Gryffindor.")
    elif name_length == 5:
        print(f"{name} goes to Slytherin.")
    elif name_length == 6:
        print(f"{name} goes to Ravenclaw.")
    elif name_length > 5:
        print(f"{name} goes to Hufflepuff.")

if all_sorted:
    print("Welcome to Hogwarts.")
