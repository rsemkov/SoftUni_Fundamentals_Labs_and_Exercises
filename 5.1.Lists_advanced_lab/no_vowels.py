string_input = input()

new_list = [x for x in string_input if x not in "aAeEiIoOuU"]

print("".join(new_list))