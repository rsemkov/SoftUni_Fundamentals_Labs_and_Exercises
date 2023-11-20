def shoot(the_index, the_power):
    global targets_input
    if valid_index_checker(the_index):
        targets_input[the_index] -= the_power
        if targets_input[the_index] <= 0:
            targets_input.pop(the_index)
    return targets_input


def add(the_index, the_value):
    global targets_input
    if valid_index_checker(the_index):
        targets_input.insert(the_index, the_value)
    else:
        print("Invalid placement!")
    return targets_input


def strike(the_index, the_radius):
    global targets_input
    start_index = the_index - the_radius
    end_index = the_index + the_radius
    if valid_index_checker(start_index) and valid_index_checker(end_index):
        targets_input = targets_input[:start_index] + targets_input[end_index + 1:]
    else:
        print("Strike missed!")
    return targets_input


def valid_index_checker(idx):
    global targets_input
    if 0 <= idx < len(targets_input):
        return True
    else:
        return False


targets_input = [int(x) for x in input().split()]

while True:
    command = input()
    if command == "End":
        break

    command = command.split()
    action, index, value = command[0], int(command[1]), int(command[2])

    if action == "Shoot":
        targets_input = shoot(index, value)
    elif action == "Add":
        targets_input = add(index, value)
    elif action == "Strike":
        targets_input = strike(index, value)

targets_input = [str(a) for a in targets_input]
print("|".join(targets_input))
