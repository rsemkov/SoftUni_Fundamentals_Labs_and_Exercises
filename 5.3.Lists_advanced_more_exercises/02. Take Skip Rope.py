string_input = input()
nums_list = [int(x) for x in string_input if x.isdigit()]
non_nums_list = [y for y in string_input if not y.isdigit()]

take_list = []
skip_list = []
for index, num in enumerate(nums_list):
    if index % 2 == 0:
        take_list.append(num)
    else:
        skip_list.append(num)

result_string = ""
for idx in range(len(take_list)):
    count_to_take = take_list[idx]
    count_to_skip = skip_list[idx]

    for _ in range(count_to_take):
        if len(non_nums_list) > 0:
            result_string += non_nums_list.pop(0)

    for _ in range(count_to_skip):
        if len(non_nums_list) > 0:
            non_nums_list.pop(0)

print(result_string)
