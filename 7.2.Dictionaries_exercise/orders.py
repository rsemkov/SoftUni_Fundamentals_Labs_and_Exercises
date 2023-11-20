items_dict = {}

while True:
    command = input()
    if command == "buy":
        break

    command = command.split()

    product = command[0]
    # THE VALUE IS LIST CONTAINING THE PRICE AND QUANTITY
    value = [float(command[1]), int(command[2])]
    price = value[0]
    quantity = value[1]

    # IF THE PRODUCT IS EXISTING IN THE DICTIONARY, WE REPLACE THE PRICE, AND ADD THE QUANTITY TO THE EXISTING QUANTITY
    if product in items_dict:
        items_dict[product][0] = price
        items_dict[product][1] += quantity
    else:
        items_dict[product] = value

for product_name, total_cost in items_dict.items():
    total_cost = total_cost[0] * total_cost[1]
    print(f"{product_name} -> {total_cost:.2f}")
