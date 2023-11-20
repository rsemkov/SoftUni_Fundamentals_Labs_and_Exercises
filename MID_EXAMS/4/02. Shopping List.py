def urgent(the_item, the_list):
    if the_item not in the_list:
        the_list.insert(0, the_item)
    return the_list


def unnecessary(the_item, the_list):
    while the_item in the_list:
        the_list.remove(the_item)
    return the_list


def correct(old_item, new_item, the_list):
    for index, items in enumerate(the_list):
        if items == old_item:
            the_list[index] = new_item
    return the_list


def rearrange(the_item, the_list):
    if the_item in the_list:
        for index, items in enumerate(the_list):
            if items == the_item:
                the_list.append(the_list.pop(index))
    return the_list


groceries_list = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break
    command = command.split()
    action = command[0]
    item = command[1]

    if action == "Urgent":
        groceries_list = urgent(item, groceries_list)
    elif action == "Unnecessary":
        groceries_list = unnecessary(item, groceries_list)
    elif action == "Correct":
        the_new_item = command[2]
        groceries_list = correct(item, the_new_item, groceries_list)
    elif action == "Rearrange":
        groceries_list = rearrange(item, groceries_list)


print(", ".join(groceries_list))

