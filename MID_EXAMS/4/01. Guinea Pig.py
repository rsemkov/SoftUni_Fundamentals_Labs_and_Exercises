food_quantity = float(input())*1000
hay_quantity = float(input())*1000
cover_quantity = float(input())
weight_in_kg = float(input())

enough_food = True
for day in range(1, 31):
    food_quantity -= 300
    if day % 2 == 0:
        hay_quantity -= food_quantity * 0.05
    if day % 3 == 0:
        cover_quantity -= weight_in_kg / 3

    if food_quantity <= 0 or hay_quantity <= 0 or cover_quantity <= 0:
        enough_food = False
        break

if enough_food:
    print(f"Everything is fine! Puppy is happy! Food: {food_quantity/1000:.2f}, Hay: {hay_quantity/1000:.2f}, Cover: {cover_quantity:.2f}.")
else:
    print("Merry must go to the pet store!")
