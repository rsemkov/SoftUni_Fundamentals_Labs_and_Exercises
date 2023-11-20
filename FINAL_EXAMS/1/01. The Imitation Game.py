def move(letters_count, the_list):

    first_half = the_list[:letters_count]
    second_half = the_list[letters_count:]
    the_list = second_half + first_half
    return the_list


def insert(idx, value, the_list):
    the_list = the_list[:idx] + list(value) + the_list[idx:]
    return the_list


def change_all(substring, replacement, the_list):
    for index, item in enumerate(the_list):
        if item == substring:
            the_list[index] = replacement
    return the_list


initial_list = [x for x in input()]
while True:
    command = input()
    if command == "Decode":
        break
    command = command.split('|')
    action = command[0]

    if action == "Move":
        letters_num = int(command[1])
        initial_list = move(letters_num, initial_list)

    elif action == "Insert":
        the_index = int(command[1])
        the_value = command[2]
        initial_list = insert(the_index, the_value, initial_list)

    elif action == "ChangeAll":
        the_substring = command[1]
        the_replacement = command[2]
        initial_list = change_all(the_substring, the_replacement, initial_list)


message_output = "".join(initial_list)
print(f"The decrypted message is: {message_output}")
