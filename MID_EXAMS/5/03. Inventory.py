inventory_items = [_ for _ in input().split(", ")]

while True:
    command = input()
    if command == "Craft!":
        break
    command = command.split(" - ")
    action = command[0]
    item_or_items = command[1]

    if action == "Collect":
        if item_or_items in inventory_items:
            continue
        inventory_items.append(item_or_items)

    elif action == "Drop":
        if item_or_items not in inventory_items:
            continue
        for index, item in enumerate(inventory_items):
            if item == item_or_items:
                inventory_items.pop(index)

    elif action == "Renew":
        if item_or_items not in inventory_items:
            continue
        for index, item in enumerate(inventory_items):
            if item == item_or_items:
                inventory_items.pop(index)
                inventory_items.append(item)

    else:  # COMBINE
        item_or_items = item_or_items.split(":")
        old_item = item_or_items[0]
        new_item = item_or_items[1]
        if old_item not in inventory_items:
            continue

        for index, item in enumerate(inventory_items):
            if item == old_item:
                inventory_items.insert(index + 1, new_item)

print(", ".join(inventory_items))
