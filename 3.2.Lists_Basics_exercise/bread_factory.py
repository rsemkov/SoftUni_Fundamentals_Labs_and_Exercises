str_input = input().split("|")

energy = 100
coins = 100
success_y_n = True

for event in str_input:
    if "rest" in event:
        pts_energy = event.split("-")
        energy_gained = int(pts_energy[1])
        energy += energy_gained
    
        if energy > 100:
            energy_gained = 100 - (energy - int(pts_energy[1]))
            energy = 100

        print(f"You gained {energy_gained} energy.")
        print(f"Current energy: {energy}.")

    elif "order" in event:
        if energy >= 30:
            energy -= 30
            coins_gained = event.split("-")
            coins += int(coins_gained[1])
            print(f"You earned {int(coins_gained[1])} coins.")
        else:
            energy += 50
            if energy > 100:
                energy = 100
            print("You had to rest!")

    else:
        coins_spent = event.split("-")
        if int(coins_spent[1]) <= coins:
            coins -= int(coins_spent[1])
            print(f"You bought {coins_spent[0]}.")
        else:
            print(f"Closed! Cannot afford {coins_spent[0]}.")
            success_y_n = False
            break

if success_y_n:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

