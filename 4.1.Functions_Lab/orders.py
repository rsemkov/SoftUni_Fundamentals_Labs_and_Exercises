COFFEE_PRICE = 1.50
WATER_PRICE = 1.00
COKE_PRICE = 1.40
SNACKS_PRICE = 2.00


def total_price(product, quantity):
    if product == "coffee":
        return COFFEE_PRICE * quantity
    elif product == "water":
        return WATER_PRICE * quantity
    elif product == "coke":
        return COKE_PRICE * quantity
    elif product == "snacks":
        return SNACKS_PRICE * quantity


product_input = input()
quantity_input = int(input())
total = total_price(product_input, quantity_input)
print(f"{total:.2f}")
