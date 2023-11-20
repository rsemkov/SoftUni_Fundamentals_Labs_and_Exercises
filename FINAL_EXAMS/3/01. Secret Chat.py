def insert_space(index, the_string):
    the_string = the_string[:index] + " " + the_string[index:]
    print(the_string)
    return the_string


def reverse(the_substring, the_string):
    if the_substring in the_string:
        the_string = the_string.replace(the_substring, "", 1)
        the_string = the_string + the_substring[-1::-1]
        print(the_string)
    else:
        print("error")
    return the_string


def change_all(the_substring, the_replacement, the_string):
    the_string = the_string.replace(the_substring, the_replacement)
    print(the_string)
    return the_string


def main():
    concealed_message = input()
    while True:
        command = input()
        if command == "Reveal":
            break
        command = command.split(":|:")
        action = command[0]
        if action == "InsertSpace":
            idx = int(command[1])
            concealed_message = insert_space(idx, concealed_message)
        elif action == "Reverse":
            substring = command[1]
            concealed_message = reverse(substring, concealed_message)
        elif action == "ChangeAll":
            substring = command[1]
            replacement = command[2]
            concealed_message = change_all(substring, replacement, concealed_message)

    print(f"You have a new text message: {concealed_message}")


main()
