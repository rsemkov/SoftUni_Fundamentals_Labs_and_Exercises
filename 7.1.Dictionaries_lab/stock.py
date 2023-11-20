dict_values_input = input().split()
products_searched_for = input().split()

my_dict = {}

for index in range(0, len(dict_values_input), 2):
    key_to_add = dict_values_input[index]
    value_to_add = int(dict_values_input[index+1])

    my_dict[key_to_add] = value_to_add

for item in products_searched_for:
    if item in my_dict.keys():
        quantity = my_dict[item]
        print(f"We have {quantity} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")

