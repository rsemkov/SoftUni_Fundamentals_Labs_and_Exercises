first_string_input = input()
second_string_input = input()

while first_string_input in second_string_input:
    second_string_input = second_string_input.replace(first_string_input, "")

print(second_string_input)