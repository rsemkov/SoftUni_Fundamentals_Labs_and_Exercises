initial_energy = int(input())

won_battles_counter = 0
enough_energy = True

while True:
    command = input()

    if command == "End of battle":
        break

    if initial_energy <= 0:
        enough_energy = False
        break

    distance_to_enemy = int(command)

    if distance_to_enemy > initial_energy:
        enough_energy = False
        break

# IF YOU WIN A BATTLE/REACH AN ENEMY:
    won_battles_counter += 1
    initial_energy -= distance_to_enemy

    if won_battles_counter % 3 == 0 and won_battles_counter != 0:
        initial_energy += won_battles_counter

if enough_energy:
    print(f"Won battles: {won_battles_counter}. Energy left: {initial_energy}")
else:
    print(f"Not enough energy! Game ends with {won_battles_counter} won battles and {initial_energy} energy")
