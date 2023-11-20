def value_calculator(the_item):
    letter_before = the_item[0]
    letter_after = the_item[-1]
    the_number = int(the_item[1:-1])
    # operations done on first letter:
    if letter_before.isupper():
        the_number /= (ord(letter_before) - 64)
    else:
        the_number *= (ord(letter_before) - 96)
    # operations done on last letter
    if letter_after.isupper():
        the_number -= (ord(letter_after) - 64)
    else:
        the_number += (ord(letter_after) - 96)
    return the_number


str_input = [x.strip() for x in input().split()]
result = 0
for item in str_input:
    result += value_calculator(item)

print(f"{result:.2f}")
