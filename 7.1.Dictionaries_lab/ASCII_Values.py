chars_input = input().split(", ")

chars_dict = {}
for char in chars_input:
    key = char
    value = ord(char)

    chars_dict[key] = value

print(chars_dict)
