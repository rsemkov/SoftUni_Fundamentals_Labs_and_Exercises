string_input = input()

digits_list = []
letters_list = []
others_list = []

for char in string_input:
    if char.isdigit():
        digits_list.append(char)
    elif char.isalpha():
        letters_list.append(char)
    else:
        others_list.append(char)

print("".join(digits_list))
print("".join(letters_list))
print("".join(others_list))



