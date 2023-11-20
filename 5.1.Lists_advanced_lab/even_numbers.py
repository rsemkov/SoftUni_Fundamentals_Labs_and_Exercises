numbers_input = input().split(", ")

even_indexes_list = [index for index, x in enumerate(numbers_input) if int(x) % 2 == 0]

print(even_indexes_list)
