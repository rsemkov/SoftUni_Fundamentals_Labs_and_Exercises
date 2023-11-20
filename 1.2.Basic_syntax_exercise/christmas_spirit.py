quantity = int(input())
days_left = int(input())

total_cost = 0
total_spirit = 0

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

if days_left % 10 == 0:
    total_spirit -= 30

for i in range(1, days_left + 1):
    if i % 11 == 0:
        quantity += 2

    if i % 2 == 0:
        total_cost += ornament_set * quantity
        total_spirit += 5
    if i % 3 == 0:
        total_cost += (tree_skirt + tree_garlands) * quantity
        total_spirit += 13
    if i % 5 == 0:
        total_cost += tree_lights * quantity
        total_spirit += 17
    if i % 5 == 0 and i % 3 == 0:
        total_spirit += 30

    if i % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt + tree_garlands + tree_lights

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")




