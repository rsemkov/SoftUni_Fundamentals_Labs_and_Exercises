starting_char = ord(input())
ending_char = ord(input())
string_input = input()

chars_sum = 0
for item in string_input:
    if starting_char < ord(item) < ending_char:
        chars_sum += ord(item)

print(chars_sum)