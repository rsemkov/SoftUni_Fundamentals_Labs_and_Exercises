items_and_prices = input().split("|")
budget = float(input())
INITIAL_BUDGET = budget

CLOTHES_MAX_PRICE = 50
SHOES_MAX_PRICE = 35
ACCESSORIES_MAX_PRICE = 20.50
TICKET_COST = 150

bought_items_list = []

for action in items_and_prices:
    action = action.split("->")
    item = action[0]
    price = float(action[1])

    if (item == "Clothes" and price > CLOTHES_MAX_PRICE) or \
       (item == "Shoes" and price > SHOES_MAX_PRICE) or \
       (item == "Accessories" and price > ACCESSORIES_MAX_PRICE):
        continue

    if budget < price:
        continue

    budget -= price
    bought_items_list.append(round(price * 1.4, 2))

    print(f"{price * 1.4:.2f}", end=" ")

budget += sum(bought_items_list)
profit = budget - INITIAL_BUDGET

print("")
print(f"Profit: {profit:.2f}")

if budget >= TICKET_COST:
    print("Hello, France!")
else:
    print("Not enough money.")







