def make_upper(the_index, the_string):
    the_string = the_string[:the_index] + the_string[the_index].upper() + the_string[the_index + 1:]
    print(the_string)
    return the_string


def make_lower(the_index, the_string):
    the_string = the_string[:the_index] + the_string[the_index].lower() + the_string[the_index + 1:]
    print(the_string)
    return the_string


def insert(the_index, the_char, the_string):
    if 0 <= the_index < len(the_string):
        the_string = the_string[:the_index] + the_char + the_string[the_index:]
        print(the_string)
    return the_string


def replace(the_char, the_value, the_string):
    if the_char in the_string:
        new_symbol = chr(ord(the_char) + the_value)
        the_string = the_string.replace(the_char, new_symbol)
        print(the_string)
    return the_string


def validation(the_string):
    # CONDITION 1
    if len(the_string) < 8:
        print("Password must be at least 8 characters long!")

    # CONDITION 2
    for letter in the_string:
        if not letter.isalnum() and letter != "_":
            print("Password must consist only of letters, digits and _!")
            break

    # CONDITION 3
    upper_case_condition = False
    for item in the_string:
        if item.isalpha() and item.isupper():
            upper_case_condition = True
    if not upper_case_condition:
        print("Password must consist at least one uppercase letter!")

    # CONDITION 4
    lower_case_condition = False
    for item in the_string:
        if item.isalpha() and item.islower():
            lower_case_condition = True
    if not lower_case_condition:
        print("Password must consist at least one lowercase letter!")

    # CONDITION 5
    one_digit_condition = False
    for item in the_string:
        if item.isdigit():
            one_digit_condition = True
    if not one_digit_condition:
        print("Password must consist at least one digit!")


def main():
    initial_string = input()
    while True:
        command = input()
        if command == "Complete":
            break
        command = command.split()
        action = command[0]
        if action == "Make":
            idx = int(command[2])
            if command[1] == "Upper":
                initial_string = make_upper(idx, initial_string)
            else:  # Lower
                initial_string = make_lower(idx, initial_string)
        elif action == "Insert":
            idx = int(command[1])
            char = command[2]
            initial_string = insert(idx, char, initial_string)
        elif action == "Replace":
            char = command[1]
            value = int(command[2])
            initial_string = replace(char, value, initial_string)
        elif action == "Validation":
            validation(initial_string)


main()
