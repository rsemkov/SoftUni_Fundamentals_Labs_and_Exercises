def out_of_stock(gift, iterable_list):
    while gift in iterable_list:
        index = iterable_list.index(gift)
        iterable_list[index] = "None"
    return iterable_list


def required(gift, index, iterable_list):
    if 0 <= index < len(iterable_list):
        iterable_list[index] = gift
    return iterable_list


def just_in_case(gift, iterable_list):
    iterable_list[-1] = gift
    return iterable_list


gift_names_input = input().split()
while True:
    command = input()
    if command == "No Money":
        break

    command = command.split()
    action = command[0]
    gifts = command[1]

    if action == "OutOfStock":
        gift_names_input = out_of_stock(gifts, gift_names_input)
    elif action == "Required":
        idx = int(command[2])
        gift_names_input = required(gifts, idx, gift_names_input)
    else:
        gift_names_input = just_in_case(gifts, gift_names_input)

for item in gift_names_input:
    if item != "None":
        print(item, end=" ")
