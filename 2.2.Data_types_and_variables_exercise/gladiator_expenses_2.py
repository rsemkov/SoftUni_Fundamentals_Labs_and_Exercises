lost_fights_count = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_shield_counter = 0
total_expenses = 0

for fights in range(1, lost_fights_count + 1):
    if fights % 2 == 0:
        total_expenses += helmet_price

    if fights % 3 == 0:
        total_expenses += sword_price

    if fights % 6 == 0:
        total_expenses += shield_price
        broken_shield_counter += 1

    if fights % 12 == 0:
        total_expenses += armor_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")
