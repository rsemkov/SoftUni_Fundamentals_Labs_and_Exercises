def take_odd(the_string):
    new_pass = ""
    for index, ch in enumerate(the_string):
        if index % 2 != 0:
            new_pass += ch
    print(new_pass)
    return new_pass


def cut(the_index, the_len, the_string):
    part_to_remove = the_string[the_index: the_index + the_len]
    the_string = the_string.replace(part_to_remove, "", 1)
    print(the_string)
    return the_string


def substitute(the_substring, the_substitute, the_string):
    if the_substring in the_string:
        the_string = the_string.replace(the_substring, the_substitute)
        print(the_string)
    else:
        print("Nothing to replace!")
    return the_string


string_input = input()
while True:
    command = input()
    if command == "Done":
        break
    command = command.split()
    action = command[0]

    if action == "TakeOdd":
        string_input = take_odd(string_input)
    elif action == "Cut":
        idx = int(command[1])
        length = int(command[2])
        string_input = cut(idx, length, string_input)
    elif action == "Substitute":
        substring_input = command[1]
        substitute_input = command[2]
        string_input = substitute(substring_input, substitute_input, string_input)

print(f"Your password is: {string_input}")
