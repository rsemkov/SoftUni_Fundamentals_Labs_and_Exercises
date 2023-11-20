def add_stop(index, to_insert, the_string):
    if 0 <= index < len(the_string):
        the_string = the_string[:index] + to_insert + the_string[index:]
    print(the_string)
    return the_string


def remove_stop(start, stop, the_string):
    if (0 <= start < len(the_string)) and (0 <= stop < len(the_string)):
        the_string = the_string[:start] + the_string[stop + 1:]
    print(the_string)
    return the_string


def switch(old, new, the_string):
    if old in the_string:
        the_string = the_string.replace(old, new)
    print(the_string)
    return the_string


initial_str = input()
while True:
    command = input()
    if command == "Travel":
        break
    command = command.split(":")
    action = command[0]
    if action == "Add Stop":
        idx = int(command[1])
        to_add = command[2]
        initial_str = add_stop(idx, to_add, initial_str)
    elif action == "Remove Stop":
        start_idx = int(command[1])
        stop_idx = int(command[2])
        initial_str = remove_stop(start_idx, stop_idx, initial_str)
    elif action == "Switch":
        old_string = command[1]
        new_string = command[2]
        initial_str = switch(old_string, new_string, initial_str)

print(f"Ready for world tour! Planned stops: {initial_str}")

