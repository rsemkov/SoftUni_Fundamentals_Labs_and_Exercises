def loot(loot_items, the_list):
    for item in loot_items:
        if item not in the_list:
            the_list.insert(0, item)
    return the_list


def drop(index, the_list):
    if 0 <= index < len(the_list):
        item = the_list.pop(index)
        the_list.append(item)
    return the_list


def steal(count, the_list):
    stolen_items = []
    if count >= len(the_list):
        print(", ".join(the_list))
        the_list.clear()
    else:
        for _ in range(count):
            stolen_items.append(the_list.pop())
        print(", ".join(stolen_items[-1::-1]))
    return the_list


initial_chest = input().split("|")

while True:
    command = input()
    if command == "Yohoho!":
        break

    command = command.split()
    action = command[0]

    if action == "Loot":
        items = command[1::]
        initial_chest = loot(items, initial_chest)
    elif action == "Drop":
        idx = int(command[1])
        initial_chest = drop(idx, initial_chest)
    elif action == "Steal":
        items_count = int(command[1])
        initial_chest = steal(items_count, initial_chest)

total_gain = 0
for treasure in initial_chest:
    total_gain += len(treasure)

if len(initial_chest) == 0:
    print("Failed treasure hunt.")
else:
    average_gain = total_gain / len(initial_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")