def char_multiplier(str_1, str_2):
    total_sum = 0
    while str_1 and str_2:  # while len(str_1) > 0 and len(str_2) > 0
        total_sum += ord(str_1.pop(0)) * ord(str_2.pop(0))

    for ch in str_1:
        total_sum += ord(ch)
    for ch in str_2:
        total_sum += ord(ch)
    return total_sum


strings_input = input().split()
first_str = [str(x) for x in strings_input[0]]
second_str = [str(x) for x in strings_input[1]]
result = char_multiplier(first_str, second_str)
print(result)
