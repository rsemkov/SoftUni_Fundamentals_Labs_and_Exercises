my_dict = {}

while True:
    command = input()
    if command == "statistics":
        break

    value = command.split(": ")

    item = value[0]
    quantity = int(value[1])

    if item not in my_dict:
        my_dict[item] = quantity
    else:
        my_dict[item] += quantity
# CONVERTS THE KEYS AND VALUES OF THE DICTIONARY TO 2 SEPARATE LISTS
my_list_keys = list(my_dict.keys())
my_list_values = list(my_dict.values())

print('Products in stock:')
for index in range(len(my_list_keys)):
    print(f'- {my_list_keys[index]}: {my_list_values[index]}')
print(f'Total Products: {len(my_dict)}')
print(f'Total Quantity: {sum(my_dict.values())}')
