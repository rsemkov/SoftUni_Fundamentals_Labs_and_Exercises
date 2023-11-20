def contains(the_substring, the_activation_key):
    if the_substring in the_activation_key:
        print(f"{the_activation_key} contains {the_substring}")
    else:
        print("Substring not found!")


def flip(upper_or_lower, start, end, the_activation_key):
    substring = the_activation_key[start:end]
    if upper_or_lower == "Upper":
        the_activation_key = the_activation_key[0:start] + substring.upper() + the_activation_key[end:]
    else:  # == "Lower"
        the_activation_key = the_activation_key[0:start] + substring.lower() + the_activation_key[end:]
    print(the_activation_key)
    return the_activation_key


def slicer(start, end, the_activation_key):
    the_activation_key = the_activation_key[:start] + the_activation_key[end:]
    print(the_activation_key)
    return the_activation_key


def main():
    activation_key = input()
    while True:
        command = input()
        if command == "Generate":
            break
        command = command.split(">>>")
        action = command[0]

        if action == "Contains":
            substring = command[1]
            contains(substring, activation_key)
        elif action == "Flip":
            upper_lower = command[1]
            start_idx = int(command[2])
            end_idx = int(command[3])
            activation_key = flip(upper_lower, start_idx, end_idx, activation_key)
        elif action == "Slice":
            start_idx = int(command[1])
            end_idx = int(command[2])
            activation_key = slicer(start_idx, end_idx, activation_key)

    print(f"Your activation key is: {activation_key}")


main()
